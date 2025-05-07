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
CREATE TABLE IF NOT EXISTS tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    genre VARCHAR(100) DEFAULT NULL,
    play_count INT DEFAULT NULL,
    listeners INT DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
"""
# Execute the SQL statement
mycursor.execute(sql)

# Close cursor and connection
mycursor.close()
connection.close()
