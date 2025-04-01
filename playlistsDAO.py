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
            
    def createUser(self, user):
        """Insert a new user into the users table."""
        cursor = self.getcursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (user["name"], user["email"])
        cursor.execute(sql, values)
        self.connection.commit()

        # Get the newly created user ID
        user["id"] = cursor.lastrowid

        self.close()
        return user
    
    def createTrack(self, track):
        """Insert a new track into the tracks table."""
        cursor = self.getcursor()
        sql = """
            INSERT INTO tracks (title, artist, genre, playcount, listeners) 
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            track["title"], 
            track["artist"], 
            track.get("genre"),  # Use .get() to handle NULL values
            track.get("playcount"), 
            track.get("listeners")
        )
        cursor.execute(sql, values)
        self.connection.commit()

        # Get the newly created track ID
        track["id"] = cursor.lastrowid

        self.close()
        return track
    

PlaylistsDAO = PlaylistsDAO()

if __name__ == "__main__":
    
    # Example Usage:
    #dao = PlaylistsDAO()
    #new_user = {"name": "Natan","email":"natan@gmail.com"}
    #created_user = PlaylistsDAO.createUser(new_user)
    #print(created_user)  # Output: {'name': 'Alice', 'id': 1}
# Example Usage:


    # Example track data without explicitly setting None
    new_track = {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        # genre, playcount, listeners are omitted, so they will default to NULL in the database
    }
    # Create the track
    created_track = PlaylistsDAO.createTrack(new_track)
    # Print the result
    print(created_track)  # Expected output: {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'id': <generated_id>}
