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

The Music Playlist Organiser will be developed to demonstrate the techniques and knowledge covered in the Web Services and Application module. It will showcase key concepts like CRUD operations, API integration, dynamic web interfaces using Flask and AJAX, and database management with MySQL. Additionally, the project will highlight practical skills in hosting applications (on PythonAnywhere) and using third-party APIs, like Last.fm, to enhance user experience and functionality.<br>
[🔝 Back to Top](#table-of-contents)





## Project Description 
A Music Playlist Organizer is a web app that enables a single operator to create and manage playlists efficiently. The project includes CRUD operations for playlists and tracks, along with an intuitive web interface for easy interaction. The integration of the Last.fm API enhances the experience by automatically fetching song details.

---

### 📌 Features Breakdown

### 1. Core Features

- **✔ CRUD Operations for Playlists and Tracks:**
  - The operator can Create, Read, Update, and Delete playlists.
  - Each playlist contains multiple tracks.
  - Tracks can be added to or removed from playlists.
  
- **✔ Database Structure:**
  - A table for playlists storing metadata (title, creation date, etc.).
  - A table for tracks storing unique song details (title, artist, genre).
  - A join table to allow tracks to be added multiple times to the same or different playlists.
  
- **✔ Web Interface (AJAX & Flask):**
  - A clean and interactive UI for managing playlists and tracks.
  - AJAX calls enable dynamic updates without reloading the page.

---

#### 2. Advanced Features 

- **🟢 Last.fm API Integration:**
    - Fetch song details automatically.

- **🟢 Visualisation & Statistics:**
  - Graphs displaying top genres, most frequently added artists, and playlist trends.
  - Pie charts or bar graphs to visualize playlist composition.

- **🟢 Hosting on PythonAnywhere:**
  - Deployment online for accessibility and evaluation.
  - MySQL for database management.

---

### ![](img/database-storage32x32.png) Database Schema Example

### 1. Playlists Table
Stores playlist details.

| id  | name         | created_at          |
|-----|-------------|---------------------|
| 1   | Chill Vibes | 2025-03-25 10:00:00 |
| 2   | Workout Mix | 2025-03-26 11:00:00 |

### 2. Tracks Table
Stores unique track details.

| id  | title             | artist       | genre    |
|-----|------------------|-------------|---------|
| 1   | Blinding Lights | The Weeknd  | Pop     |
| 2   | Lose Yourself   | Eminem      | Hip-Hop |
| 3   | Eye of the Tiger | Survivor   | Rock    |

### 3. Playlist Tracks Table (Join Table)
Allows tracks to be added multiple times to the same or different playlists.

| id  | playlist_id | track_id | added_at          |
|-----|------------|---------|------------------|
| 1   | 1          | 1       | 2025-03-26 10:00 |
| 2   | 1          | 1       | 2025-03-26 10:05 |
| 3   | 2          | 1       | 2025-03-27 12:30 |
| 4   | 1          | 2       | 2025-03-28 15:20 |
| 5   | 2          | 2       | 2025-03-28 16:40 |

## How This Works
- The `tracks` table stores unique song details.
- The `playlist_tracks` table records which tracks belong to which playlists.
- The same track can appear:
  - Multiple times in the same playlist (each entry in `playlist_tracks` is unique).
  - In multiple different playlists.
- The Flask API enables seamless communication between the frontend and the database.

## Benefits of This Approach
✅ Allows the same track to be added multiple times to the same playlist.  
✅ Enables tracks to exist in multiple playlists efficiently.  
✅ Reduces data duplication by storing unique track details separately.  
✅ Improves performance and query optimization.  
✅ Enhances flexibility for future extensions, such as play counts and user interactions.  
✅ Provides a structured and maintainable API for frontend integration.


---

### 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript (AJAX)
- **Database:** MySQL
- **API Integration:** Last.fm API

---

### 📝 Potential Challenges

- **Rate Limits:** The Last.fm API has request limits, so caching or request optimization may be required.
- **Database Performance:** Optimizing queries to handle a large number of tracks efficiently.
- **Frontend-Backend Communication:** Ensuring smooth integration between AJAX requests and Flask API responses.

---

## Files and Structure

The repository includes the following files and structure:




[🔝 Back to Top](#table-of-contents)

## Getting Started

To get started with this project, clone the repository to your local machine.




[🔝 Back to Top](#table-of-contents)

## License

This repository is licensed under the MIT License - see the LICENSE file for more details.<br>
[🔝 Back to Top](#table-of-contents)

## Acknowledgments

The Music Playlist Organiser project has been developed to demonstrate the techniques and concepts covered in the Web Services and Application module. It highlights the implementation of CRUD operations, third-party API integration (such as the Last.fm API), dynamic web interfaces using Flask and AJAX, and database management with MySQL. The project also emphasises practical experience in hosting applications on PythonAnywhere.
Special thanks are due to the lecturer for providing valuable guidance and resources throughout the module, enabling the application of theoretical knowledge to a real-world project. Furthermore, web resources like the Last.fm API documentation and online hosting services have played a crucial role in enhancing the development experience.<br>
[🔝 Back to Top](#table-of-contents)

## Author

I am a student at Atlantic Technical University in Ireland, currently pursuing a Higher Diploma in Science in Computing (Data Analytics). I have a strong foundation in computing with a particular focus on data analysis and web services. My technical skills include:

* **Operating Systems**: Proficient in the Windows family and Linux (especially Ubuntu).
* **Programming**: Python programming with a focus on data analysis and web development.
* **Databases**: Basic knowledge of MySQL for data storage and management.
* **Web Technologies**: Familiar with Apache for web server management, and Flask for building dynamic web applications.
* **Scripting**: Experience with Bash scripting and YAML for automation and configuration.
* **Web Services**: Practical experience in creating and managing web applications with CRUD operations, dynamic interfaces using **AJAX**, and third-party API integration (such as **Last.fm API**).

I am enthusiastic and hardworking, passionate about analysing real-world and virtual datasets. I enjoy working on data-driven projects that provide insights and drive decisions.<br>
[🔝 Back to Top](#table-of-contents)