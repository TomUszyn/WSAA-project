import os
import mysql.connector
from dotenv import load_dotenv
import requests

class PlaylistsDAO:
    
    ## Initialize the database connection using environment variables.
    def __init__(self):
        """Initialize database connection using environment variables."""
        load_dotenv()  # Load from .env in the same directory

        # Get DB settings from environment variables
        self.host = os.getenv("DB_HOST")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.API_key = os.getenv("API_KEY")
        self.URL = "http://ws.audioscrobbler.com/2.0/"

        self.connection = None
        self.cursor = None
        
    # Establish a database connection and return a cursor
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
    
    # Close cursor and connection
    def close(self):
        """Close cursor and connection if open."""
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None
            
    # Get all tracks        
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
    
    # Find a track by ID
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
    
    # Check if a track is a duplicate based on title and artist
    def isDuplicateTrack(self, title, artist, closeAfter=True):
        cursor = self.getcursor()
        sql = """
            SELECT COUNT(*) 
            FROM tracks 
            WHERE title = %s AND artist = %s
        """
        cursor.execute(sql, (title, artist))
        result = cursor.fetchone()
        if closeAfter:
            self.close()
        return result[0] > 0
    
    # Find existing track by title and artist
    def findExistingTrack(self, title, artist, closeAfter=True):
       cursor = self.getcursor()
       sql = """
           SELECT * FROM tracks 
           WHERE title = %s AND artist = %s
           LIMIT 1
       """
       cursor.execute(sql, (title, artist))
       result = cursor.fetchone()
       if closeAfter:
           self.close()
       return self.convertToDictionary(result) if result else None
   
    # Fetch track information from Last.fm API using artist and title
    def getTrackInfo(self, artist, title):
        """Fetch track information from Last.fm API"""
        params = {
            'method': 'track.getInfo',
            'api_key': self.API_key,
            'artist': artist,
            'track': title,
            'format': 'json'
        }
        response = requests.get(self.URL, params=params)
        data = response.json()
        if 'track' in data:
            return data['track']
        return None

    # Create a new track with duplication check and auto-fill missing fields using Last.fm API
    def createTrack(self, track):
        """Insert a new track into the tracks table with duplication check."""
        if self.isDuplicateTrack(track["title"], track["artist"]):
            existing = self.findExistingTrack(track["title"], track["artist"])
            raise ValueError(f"Track already exists with ID {existing['id']}")
        
        # Auto-fill missing fields using Last.fm
        info = self.getTrackInfo(track["artist"], track["title"])
        if info:
            if "genre" not in track or not track.get("genre"):
                if "toptags" in info and "tag" in info["toptags"] and info["toptags"]["tag"]:
                    track["genre"] = info["toptags"]["tag"][0]["name"]
            if "play_count" not in track or not track.get("play_count"):
                track["play_count"] = int(info.get("playcount", 0))
            if "listeners" not in track or not track.get("listeners"):
                track["listeners"] = int(info.get("listeners", 0))

        cursor = self.getcursor()
        sql = """
            INSERT INTO tracks (title, artist, genre, play_count, listeners)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            track["title"],
            track["artist"],
            track.get("genre"),
            track.get("play_count", 0),
            track.get("listeners", 0)
        )
        cursor.execute(sql, values)
        self.connection.commit()
        track["id"] = cursor.lastrowid
        self.close()
        return track
    
    # Update an existing track with duplication check    
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
        
        # Duplication check
        if (title != current[1] or artist != current[2]) and \
           self.isDuplicateTrack(title, artist, closeAfter=False):
            print("Updated values would create duplicate track.")
            self.close()
            raise ValueError("Updated values would create a duplicate track.")

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
    
    # Delete a track by ID
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



dao = PlaylistsDAO()

#if __name__ == "__main__":
    
    #### Test: Create Track ###
#   try:
#       new_track = {
#           "title": "Kayleigh",
#           "artist": "Marillion",       
#       }
#       created_track = dao.createTrack(new_track)
#       print("Created:", created_track)
#   except ValueError as e:
#       print("Create Track Error:", e)



   #### Test: Get All Tracks ####
#    try:
#        all_tracks = dao.getAll()
#        print("All Tracks:", all_tracks)
#    except Exception as e:
#        print("Get All Error:", e)
        
   
   
   #### Test: Find by ID ####
    
#   track_id = 1
#   track = dao.findByID(track_id)
#   if track:
#       print("Track found:", track)
#   else:
#       print(f"No track found with ID {track_id}.")
    

   #### Test: Update Track ####
#   track_id = 3
#   update_data = {
#       "title": "Updated Title",
#       "genre": "Pop Rock",
#       "play_count": 1600000
#   }
#   
#   try:
#       updated_track = dao.update(track_id, update_data)
#       print("Updated:", updated_track)
#   except ValueError as e:
#       print("Update Error:", e)



   # === Test: Delete Track ===
#    track_id = 31
#    try:
#        result = dao.delete(track_id)
#        print("Delete Result:", result)
#    except Exception as e:
#        print("Delete Track Error:", e)
