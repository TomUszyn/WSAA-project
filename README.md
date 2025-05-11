# Web Services and Application  Project

This repository contains the project for the "Web Services and Application" module. 

## Table of Contents

- [About](#about)
- [Project description](#project-description)
- [Files and Structure](#files-and-structure)
- [Running the code](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## About

The Music Playlist Organiser will be developed to demonstrate the techniques and knowledge covered in the Web Services and Application module. It will showcase key concepts like CRUD operations, API integration, dynamic web interfaces using Flask and AJAX, and database management with MySQL. Additionally, the project will highlight practical skills in hosting applications (on PythonAnywhere) and using third-party APIs, like Last.fm, to enhance user experience and functionality.<br>
👉 Live Demo: [View the project on PythonAnywhere](https://tomuszyn.eu.pythonanywhere.com/)<br>
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
  - A table for playlists storing metadata (title, creation date).
  - A table for tracks storing unique song details (title, artist, genre, etc.).
  - A join table to allow tracks to be added multiple times to the same or different playlists.
  
- **✔ Web Interface (AJAX & Flask):**
  - A clean and interactive UI for managing playlists and tracks.
  - AJAX calls enable dynamic updates without reloading the page.

---

#### 2. Advanced Features 

- **🟢 Last.fm API Integration:**
    - Fetch song details automatically.

- **🟢 Hosting on PythonAnywhere:**
  - Deployment online for accessibility and evaluation.
  - MySQL for database management.

---

### ![](img/database-storage32x32.png) Database Schema Example

### 1. Playlists Table called playlists
Stores playlist details.

| id | name          | created\_at         |
| -- | ------------- | ------------------- |
| 1  | Chill Vibes   | 2025-03-25 10:00:00 |
| 2  | Workout Mix   | 2025-03-26 11:00:00 |
| 3  | Morning Tunes | 2025-03-27 08:45:12 |

### 2. Tracks Table called tracks
Stores unique track details.

| id | title            | artist     | genre   | play\_count | listeners | created\_at         |
| -- | ---------------- | ---------- | ------- | ----------- | --------- | ------------------- |
| 1  | Blinding Lights  | The Weeknd | Pop     | 1023        | 1500      | 2025-03-25 10:00:00 |
| 2  | Lose Yourself    | Eminem     | Hip-Hop | 2500        | 3200      | 2025-03-26 11:00:00 |
| 3  | Eye of the Tiger | Survivor   | Rock    | 1800        | 2200      | 2025-03-27 08:45:12 |

### 3. Playlist Tracks Table (Join Table) called playlist_tracks
Allows tracks to be added multiple times to the same or different playlists.

| id | playlist\_id | track\_id | added\_at        |
| -- | ------------ | --------- | ---------------- |
| 1  | 1            | 1         | 2025-03-25 10:00 |
| 2  | 1            | 2         | 2025-03-26 11:05 |
| 3  | 2            | 3         | 2025-03-27 08:45 |

## How This Works
- The `tracks` table stores song details.
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
[🔝 Back to Top](#table-of-contents)

## Files and Structure

The repository includes the following files and structure:

- **`.gitignore`** – Specifies files and folders to be ignored by Git version control.
- **`.env`** – Stores environment variables required for configuration.
- **`envTemplate.txt`** – Template for the `.env` file, providing guidance on required values.
- **`LICENSE`** – Legal terms and conditions for using the project.
- **`README.md`** – Documentation file providing an overview of the repository.
- **`restserver.py`** – Main server script handling API requests and responses.
- **`playlistDAO.py`** – Data Access Object for managing playlist interactions with the database.
- **`createTables/`** – Contains scripts necessary for setting up the database tables.
- **`img/`** – Directory storing images and assets used within the project.
- **`templates/`** – Contains index.html file for the application.<br>
[🔝 Back to Top](#table-of-contents)

## 🚀 Getting Started

Follow these steps to start using the Music Playlist Organiser API on your local machine.

#### 1. Clone the Repository

Clone this repository to your local environment:

```bash
git clone https://github.com/TomUszyn/WSAA-project.git
cd your-repo-name
```

#### 2. Set Up a Virtual Environment (Recommended)

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables

Create a `.env` file using the `envTemplate.txt` as a guide. This file should include your MySQL credentials and Last.fm API key.

Example `.env` content:

```ini
DB_HOST=localhost
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
LASTFM_API_KEY=your_lastfm_api_key
```

** 🔑 Important Notes:**

- **Replace all placeholder values** with your actual credentials
- **Keep this file secure** and never commit it to version control
- The `.env` file **should be in your project’s root directory**
- **Add `.env` to your `.gitignore`** to prevent accidental exposure
- **Double-check variable names** match exactly what your application expects
- **For production**, use more secure methods such as secret managers

**Obtaining a Last.fm API Key**

To get your own Last.fm API key:


1. Go to [Last.fm API Account page](https://www.last.fm/login?next=%2Fapi%2Faccount%2Fcreate%3F_pjax%3D%2523content)
2. Complete the application form with:
  - Application name
  - Description
  - Organisation (if applicable)
  - Website URL (you may use a placeholder if testing locally)
3. Accept the API Terms of Use
4. Click "Create Account"

You will receive:

- API Key (also called "Client ID")
- Shared Secret (for authentication)

** ‼️ Important Notes:**

- The API key is free for non-commercial use
- There are rate limits (typically 5 requests per second)
- For local development, you may use `http://localhost` as your callback URL
- Keep your API key secure like any other credential

#### 5. Create the MySQL Database

Before running the app, create an empty database named `your_database_name` (this should match the `DB_NAME` in your `.env` file).

**Using the MySQL CLI:**

```bash
mysql -u your_mysql_user -p
```

```sql
CREATE DATABASE your_database_name;
EXIT;
```

#### 6. Create the Tables Using Python Scripts

Run the provided Python scripts to automatically create all required tables inside your database:

```bash
# Navigate to the createTables directory
cd createTables
```

Execute each script in order:

```bash
python createTableTracks.py        # Creates the tracks table
python createTablePlaylists.py     # Creates the playlists table
python createTablesPlaylistsTracks.py  # Creates the playlist_tracks junction table
```

#### 7. Run the Flask API Server

Start the backend server:

```bash
python restserver.py
```

#### 8. Access the Web Interface

Open a web browser and navigate to:

`http://127.0.0.1:5000/`

[🔝 Back to Top](#table-of-contents)

## 📜 License

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