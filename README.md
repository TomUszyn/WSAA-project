# Web Services and Application  Project

This repository contains the project for the "Web Services and Application" module. 

## Table of Contents

- [About](#about)
- [Project description](#project-description)
- [Files and Structure](#files-and-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Running the code](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## About

The Music Playlist Organiser will be developed to demonstrate the techniques and knowledge covered in the Web Services and Application module. It will showcase key concepts like CRUD operations, API integration, dynamic web interfaces using Flask and AJAX, and database management with MySQL. Additionally, the project will highlight practical skills in hosting applications (on PythonAnywhere) and using third-party APIs, like Last.fm, to enhance user experience and functionality.



## Project Description 
A Music Playlist Organiser is a web app that enables users to create, manage, and explore their personal playlists. The project involves CRUD operations, a database for storing playlists, and an intuitive web interface for user interaction. Advanced features, such as Last.fm API integration will further enhance the user experience.

---

### 📌 Features Breakdown

#### 1. Minimum Features (Core Functionality)

- **✔ CRUD Operations for Playlists:**
    - Users can Create, Read, Update, and Delete playlists.
    - Each playlist includes a title, songs, artist names, and genres.
    - Songs can be added to or removed from a playlist.
  
- **✔ Database Structure:**
    - A table for playlists storing metadata (title, creation date, etc.).
    - A table for songs storing song details (name, artist, genre, playlist_id).
  
- **✔ Web Interface (AJAX & Flask):**
    - A clean and interactive UI for adding and managing playlists.
    - AJAX calls to perform CRUD operations dynamically.

---

#### 2. Advanced Features (For Higher Marks)

- **🟢 Last.fm API Integration:**
    - Fetch song details (artist, album, duration, release date) automatically.

- **🟢 Visualisation & Statistics:**
    - Graphs showing top genres, most played artists, and listening trends.
    - Pie charts or bar graphs to display playlist composition.

- **🟢 Hosting on PythonAnywhere:**
    - Deploy the app online for accessibility and grading purposes.
    - Use MySQL for database management.

---

### ![](img/database-storage32x32.pn)g Database Schema Example

To allow the same track to appear multiple times in a single playlist or across multiple playlists, the database schema separates track metadata from playlist entries. This is achieved through a **many-to-many relationship** between playlists and tracks.

### 1. Users Table
This table is used to separate data for different users, even without authentication.

| id  | username   | email          |
| --- | ---------- | -------------- |
| 1   | user1      | user1@email.com|
| 2   | user2      | user2@email.com|

### 2. Playlists Table
This table stores playlists for users.

| id  | name          | user_id | created_at          |
| --- | ------------- | ------- | ------------------- |
| 1   | Chill Vibes   | 1       | 2025-03-25 10:00:00 |
| 2   | Workout Mix   | 2       | 2025-03-26 11:00:00 |

### 3. Track Metadata Table
This table stores unique track details, with one entry for each track.

| id  | title           | artist       | genre    |
| --- | --------------- | ------------ | -------- |
| 1   | Blinding Lights | The Weeknd   | Pop      |
| 2   | Lose Yourself   | Eminem       | Hip-Hop  |

### 4. Playlist Tracks Table (Join Table for Many-to-Many Relationship)
This table allows a track to appear in multiple playlists.

| id  | playlist_id | track_id | added_at          |
| --- | ----------- | -------- | ----------------- |
| 1   | 1           | 1        | 2025-03-26 10:00  |
| 2   | 1           | 1        | 2025-03-26 10:05  |
| 3   | 2           | 1        | 2025-03-27 12:30  |
| 4   | 1           | 2        | 2025-03-28 15:20  |
| 5   | 2           | 2        | 2025-03-28 16:40  |

## How This Works
- The `track_metadata` table stores unique tracks.
- The `playlist_tracks` table records which tracks are in which playlists.
- The same track can appear:
  1. Multiple times in the same playlist (each entry in `playlist_tracks` is unique).
  2. In multiple different playlists.

### Benefits of This Approach
✅ The same track can be added multiple times to the same playlist.
✅ The same track can exist in multiple playlists.
✅ Efficient storage since track details (title, artist, genre, play count, listeners) are stored once.
✅ Easy to extend (e.g., add play count, listeners, etc.).

---

### 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript (AJAX)
- **Database:** MySQL
- **API Integration:** Last.fm API

---

### 📝 Potential Challenges

- **Rate Limits:** The Last.fm API has request limits, so caching or optimizing requests is important.

---

## Files and Structure

The repository includes the following files and structure:

## Getting Started

To get started with this project, clone the repository to your local machine.

## License

This repository is licensed under the MIT License - see the LICENSE file for more details.

## Acknowledgments

The Music Playlist Organiser project has been developed to demonstrate the techniques and concepts covered in the Web Services and Application module. It highlights the implementation of CRUD operations, third-party API integration (such as the Last.fm API), dynamic web interfaces using Flask and AJAX, and database management with MySQL. The project also emphasises practical experience in hosting applications on PythonAnywhere.
Special thanks are due to the lecturer for providing valuable guidance and resources throughout the module, enabling the application of theoretical knowledge to a real-world project. Furthermore, web resources like the Last.fm API documentation and online hosting services have played a crucial role in enhancing the development experience.

## Author

I am a student at Atlantic Technical University in Ireland, currently pursuing a Higher Diploma in Science in Computing (Data Analytics). I have a strong foundation in computing with a particular focus on data analysis and web services. My technical skills include:

* **Operating Systems**: Proficient in the Windows family and Linux (especially Ubuntu).
* **Programming**: Python programming with a focus on data analysis and web development.
* **Databases**: Basic knowledge of MySQL for data storage and management.
* **Web Technologies**: Familiar with Apache for web server management, and Flask for building dynamic web applications.
* **Scripting**: Experience with Bash scripting and YAML for automation and configuration.
* **Web Services**: Practical experience in creating and managing web applications with CRUD operations, dynamic interfaces using **AJAX**, and third-party API integration (such as **Last.fm API**).

I am enthusiastic and hardworking, passionate about analysing real-world and virtual datasets. I enjoy working on data-driven projects that provide insights and drive decisions.