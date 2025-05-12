# Music Playlist Organiser: User Guide  

---

## Chapter 1: Using the Application  
 
## Welcome  
This guide will help you organise music tracks and playlists efficiently. Follow the steps below to get started.  

---

## 1. Adding Tracks  
**What is a track?**  
A track represents a song (e.g., "Bohemian Rhapsody" by Queen).  

### Steps to Add a Track  
1. Click the **blue "Create" button** at the top.  
2. Fill in the required fields:  
   - **Title** (Song name)  
   - **Artist**  
3. Optional fields (you can skip these):  
   - Genre  
   - Play Count  
   - Listeners  
4. Click **Create**.  
   - *Note*: For recognised songs, genre and play data may auto-fill using **Last.fm**.  

**Validation Tips**  
- If you see **"Title is required"** or **"Artist is required"**, complete those fields.  
- For duplicates: **"This track already exists"** – adjust the title or genre.  

---

## 2. Editing or Deleting Tracks  
### Editing a Track  
1. Click the **yellow "Update" button** next to the track.  
2. Modify the details.  
3. Click **Update** to save changes.  

### Deleting a Track  
1. Click the **red "Delete" button** next to the track.  
   - *Note*: This action is immediate and permanent.  

**Important**: Each title-artist combination must be unique.  

---

## 3. Creating Playlists  
**What is a playlist?**  
A playlist is a custom collection of tracks (e.g., "Workout Mix").  

### Steps to Create a Playlist  
1. Click the **green "Create Playlist" button**.  
2. Enter a unique name (e.g., "Summer 2023").  
3. Click **Create Playlist**.  

**Validation Tips**  
- Empty names trigger: **"Playlist name is required"**.  
- Duplicate names show: **"Name already exists"**.  

---

## 4. Adding Tracks to Playlists  
1. Locate the track in the list.  
2. Click the **light blue "Add to Playlist" button**.  
3. Select a playlist from the list.  
4. Click **Add** to confirm.  

---

## 5. Managing Playlists  
### Accessing Playlists  
1. Click the **light blue "Show Playlists" button**.  

### Playlist Actions  
- **Rename**: Click the **yellow "Update" button**.  
- **Delete**: Click the **red "Delete" button** (no confirmation).  
- **View Tracks**: Click the **light blue "View Tracks" button**.  

---

## 6. Managing Playlist Contents  
### Viewing/Removing Tracks  
1. Click **View Tracks** next to a playlist.  
2. To remove a track:  
   - Click the **red "Remove" button** (instant action).  
3. Empty playlists display: **"Nothing in playlist"**.  
4. Return to the main list with **Back to Tracks**.  

---

## Last.fm Integration  
- **Automated Data**: Recognised tracks auto-fill genre, play count, and listeners via **Last.fm**.  
- **Manual Input Priority**: Your entries override auto-filled data.  
- **Limitations**: Some genres may not auto-fill.  

---

## Troubleshooting  
- **Refresh the page** or click **Back to Tracks** to reset the view.  
- Use **Update** to correct typos or details.  
- Delete incorrect entries and recreate them.  

---

## Chapter 2: Deploying the Application  
### **Deploying a Flask REST API on PythonAnywhere**  
This chapter explains how developers/administrators can deploy the backend using `venv`, GitHub, and MySQL.  

---

### 1. Account Setup  
1. Create a **PythonAnywhere account**:  
   - Visit [eu.pythonanywhere.com](https://eu.pythonanywhere.com/) and sign up.  
   - Choose a suitable plan (free tier works for testing).  

---

### 2. Clone from GitHub  
1. In your PythonAnywhere console:  
   ```bash
   cd /home/yourusername/
   git clone https://github.com/your_repo.git
   cd your_repo
   ```  

---

### 3. Virtual Environment Setup  
1. Create and activate a `venv`:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   ```  

### 4. Install Dependencies  
1. Upload `requirements.txt`:  
   ```bash
   pip install -r requirements.txt  # On PythonAnywhere
   ```  
---

### 5. Secure Environment Variables  
1. Create a `.env` file:  
   ```bash
   MYSQL_HOST="your_host"
   MYSQL_USER="your_user"
   MYSQL_PASSWORD="your_password"
   MYSQL_DB="your_database"
   ```  
2. Restrict permissions:  
   ```bash
   chmod 600 .env  # Allow only owner access
   ```  

---

### 6. MySQL Database Configuration  
1. In PythonAnywhere dashboard:  
   - Navigate to **Databases** → **Create MySQL Database**.  
   - Update `.env` with the provided credentials.  

---

### 7. Web App Configuration  
1. In PythonAnywhere **Web** tab:  
   - Choose **Manual Configuration**
   - Set **Source code** and **Working directory**: /home/yourusername/your_repo
   - **Select Python version**: Ensure Python 3.12 is selected
   - Set **working directory** to your project folder.  
2. Update the WSGI file:  
   ```python
    import sys

    project_home = '/home/yourusername/your_repo'
    if project_home not in sys.path:
        sys.path = [project_home] + sys.path

    # Import your Flask app
    from restserver import app as application
    # replace 'restserver' if your file/module name is different
    ```  


### 8. Testing & Monitoring  
1. Restart the web app and check logs:  
   - **server.log**: General server activity.  
   - **error.log**: Debugging issues.  
---

### Key Notes for Developers  
- **Security**: Never commit `.env` to GitHub.  
- **Updates**: Use `git pull` to sync code changes.  
- **Debugging**: Check PythonAnywhere logs for runtime errors.  

---

## Chapter 3: Inspirations & Credits

### 1. Conceptual Influences  
This project was fundamentally inspired by the **BookViewer API**, a minimalist CRUD (Create, Read, Update, Delete) demonstration system designed by the lecturer **Andrew Beatty** for educational purposes.

#### Core Principles Adopted:  
- **Simplicity First**: The BookViewer API’s focus on a single-table system provided a clear foundation for understanding basic database operations.  
- **CRUD Foundation**: The core structure mirrors the BookViewer’s approach to handling HTTP methods (GET, POST, PUT, DELETE).  
- **DAO Pattern**: Adopted and extended the Data Access Object layer for cleaner separation of database logic.  

#### Enhancements Beyond the Original Concept:  
| Feature               | BookViewer API (Inspiration)       | This Project (Implementation)      |  
|-----------------------|------------------------------------|------------------------------------|  
| **Scope**             | Single-table (Books)              | Multi-table (Tracks + Playlists + Playlist_Tracks)   |  
| **Data Source**       | Manual input                      | Hybrid (User + Last.fm API data)   |  
| **UI/UX**             | Terminal interface                | Web UI (Bootstrap + JavaScript)    |  
| **Backend**           | Python scripts                    | Flask REST API                     |  
| **External API Integration** | None               | Last.fm API for auto-fill          |  
#### Technology Evolution:  
- **Flask**: Replaced manual HTTP handling with a structured web framework for routing and scalability.  
- **AJAX/JavaScript**: Added dynamic UI updates without page reloads (e.g., real-time playlist edits).  
- **HTML/Bootstrap**: Transformed terminal output into responsive web pages with modern styling.  

### 2. Third-Party Tools & Libraries  
   - **[Flask](https://flask.palletsprojects.com/)**: Used for backend API development.  
  - **[Last.fm API](https://www.last.fm/api)**: Integrated for music metadata retrieval.
  - **[Bootstrap](https://getbootstrap.com/)**: Used for responsive web UI components. 

### 3 . Referneces
  - **[dotenv](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/)**: Using for load environment variables from a .env file.
  - **[virtualenvs](docs.python-guide.org/dev/virtualenvs/https://docs.python-guide.org/dev/virtualenvs/)**: Set up Virtual environment.
  - **[HTML](https://www.w3schools.com/html/)**: Useful to understand basics of HTML.
  - **[JavaScriot](https://www.w3schools.com/js/default.asp)**: Basics of JavaScript.

