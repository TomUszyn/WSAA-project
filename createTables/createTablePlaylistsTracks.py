import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Establish database connection
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Create a cursor object
mycursor = connection.cursor()

sql = """
CREATE TABLE IF NOT EXISTS playlist_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    playlist_id INT,
    track_id INT,
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE,
    FOREIGN KEY (track_id) REFERENCES tracks(id) ON DELETE CASCADE
);
"""
# Execute the SQL statement
mycursor.execute(sql)

# Close cursor and connection
mycursor.close()
connection.close()
