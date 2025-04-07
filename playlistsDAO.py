import os
import mysql.connector
from dotenv import load_dotenv

class PlaylistsDAO:
    
    def __init__(self):
        """Initialize database connection using environment variables."""
        load_dotenv()  # Load from .env in the same directory

        # Get DB settings from environment variables
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")

        self.connection = None
        self.cursor = None

    def getcursor(self):
        """Establish and return a database cursor."""
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        return self.cursor

    def close(self):
        """Close cursor and connection if open."""
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
            
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from tracks"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.close()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from tracks where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        if result:
            returnvalue = self.convertToDictionary(result)
        else:
            returnvalue = None  # handle case when no match is found
       
        self.close()
        return returnvalue

    
    def createTrack(self, track):
        """Insert a new track into the tracks table."""
        cursor = self.getcursor()
        sql = """
            INSERT INTO tracks (title, artist, genre, play_count, listeners) 
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            track["title"], 
            track["artist"], 
            track.get("genre"),  # Use .get() to handle NULL values
            track.get("play_count"), 
            track.get("listeners")
        )
        cursor.execute(sql, values)
        
        self.connection.commit()
        # Get the newly created track ID
        track["id"] = cursor.lastrowid
        self.close()
        return track
    
    def update(self, id, track):
        cursor = self.getcursor()

        # Get current data
        cursor.execute("SELECT * FROM tracks WHERE id = %s", (id,))
        current = cursor.fetchone()
        if not current:
            print("Track not found.")
            return None

        # Use current values if not provided
        title = track.get("title", current[1])
        artist = track.get("artist", current[2])
        genre = track.get("genre", current[3])
        play_count = track.get("play_count", current[4])
        listeners = track.get("listeners", current[5])

        sql = """
            UPDATE tracks 
            SET title = %s, artist = %s, genre = %s, play_count = %s, listeners = %s 
            WHERE id = %s
        """
        values = (title, artist, genre, play_count, listeners, id)

        cursor.execute(sql, values)
        self.connection.commit()
        self.close()
        return track
    
    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM tracks WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.close()
        return {"message": "Track deleted successfully."}
    
    
    def convertToDictionary(self, resultLine):
        attkeys=['id','title','artist', 'genre', 'play_count', 'listeners', 'created_at']
        track = {}
        currentkey = 0
        for attrib in resultLine:
            track[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return track



PlaylistsDAO = PlaylistsDAO()

if __name__ == "__main__":
    
    ## Example track data without explicitly setting None
    #new_track = {
    #    "title": "Bad Habits",
    #    "artist": "Ed Sheeran",
    #    # genre, playcount, listeners are omitted, so they will default to NULL in the database
    #}
    ## Create the track
    #created_track = PlaylistsDAO.createTrack(new_track)
    ## Print the result
    #print(created_track)  # Expected output: {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'id': <generated_id>}
    
    
    #track_id_to_update = 1
    #updated_data = {
    #     "genre": "Rock",
    #    }
    #result = PlaylistsDAO.update(track_id_to_update, updated_data)
    #print("Track updated:", result)
    
    
    #track_id_to_delete = 1
    #result = PlaylistsDAO.delete(track_id_to_delete) 
    #print("Track deleted:", result)
    
    #result = PlaylistsDAO.getAll()
    #print("All tracks:", result)

    idToSearch = 10
    result = PlaylistsDAO.findByID(idToSearch)

    if result:
        print(f"Track with ID {idToSearch}:", result)
    else:
        print(f"No track found with ID {idToSearch}.")
