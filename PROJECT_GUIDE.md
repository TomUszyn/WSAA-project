# Music Playlist Organiser: User Guide  

---

# Chapter 1: Using the Application  

## Welcome  
This guide will help you organise music tracks and playlists efficiently. Follow the steps below to get started.  

---

## 1. Adding Tracks  
**What is a track?**  
A track represents a song (e.g., *"Bohemian Rhapsody" by Queen*).  

### Steps to Add a Track  
1. Click the **blue "Create" button** at the top.  
   - A **form section** appears below the buttons.  
2. Fill in the required fields:  
   - **Title** (Song name)  
   - **Artist**  
3. Optional fields (you can skip these):  
   - Genre  
   - Play Count  
   - Listeners  
4. Click **Create**.  

**What Happens Next?**  
- ✅ **Success**: A popup says *"Track created successfully."*  
- ❌ **Errors**:  
  - `"Title/Artist is required"` (red text below the form).  
  - `"This track already exists"` (alert popup).  

---

## 2. Editing or Deleting Tracks  
### Editing a Track  
1. Click the **yellow "Update" button** next to the track.  
   - The **edit form** appears below the buttons.  
2. Modify details.  
3. Click **Update**.  

**What Happens Next?**  
- ✅ **Success**: *"Track updated successfully."* (popup).  
- ❌ **Error**: *"Update failed: a track with the same title and artist already exists."* (popup).  

### Deleting a Track  
1. Click the **red "Delete" button** next to the track.  
   - 🔴 **Confirmation Popup**: *"Are you sure you want to delete this track?"*  
2. Click **OK** to delete or **Cancel** to keep it.  

**What Happens Next?**  
- ✅ **Success**: *"Track deleted successfully."* (popup).  

---

## 3. Creating Playlists  
**What is a playlist?**  
A custom collection of tracks (e.g., *"Workout Mix"*).  

### Steps to Create a Playlist  
1. Click the **green "Create Playlist" button**.  
   - A **form section** appears below the buttons.  
2. Enter a unique name.  
3. Click **Create Playlist**.  

**What Happens Next?**  
- ✅ **Success**: *"Playlist created successfully."* (popup).  
- ❌ **Errors**:  
  - `"Playlist name is required"` (red text below the form).  
  - *"Playlist with this name already exists."* (popup).  

---

## 4. Adding Tracks to Playlists  
1. Click the **light blue "Add to Playlist" button** next to a track.  
   - A **list of playlists** appears.  
2. Click **Add** next to your chosen playlist.  

**What Happens Next?**  
- ✅ **Success**: *"Track added to playlist successfully."* (popup).  

---

## 5. Managing Playlists
### Accessing Playlists  
1. Click the **light blue "Show Playlists" button** at the top.  
   - This displays your existing playlists in a table.  

### Playlist Actions (After Accessing) 
- **Rename**:  
  1. Click the **yellow "Update" button** → inline form appears.  
  2. Edit the name → Click **Update Playlist**.  
  - ✅ **Success**: *"Playlist updated successfully."*  

- **Delete**:  
  1. Click the **red "Delete" button** → 🔴 **Popup**:  
     *"Are you sure you want to delete this playlist?"*  
  2. Click **OK** to delete.  
  - ✅ **Success**: *"Playlist deleted successfully."*  

- **View Tracks**: Click the **light blue "View Tracks" button**.  

---

## 6. Managing Playlist Contents  
### Removing Tracks  
1. In playlist view, click the **red "Remove" button**.  
   - 🔴 **Confirmation**: *"Are you sure you want to remove this track?"*  
2. Click **OK** to confirm.  

**What Happens Next?**  
- ✅ **Success**: *"Track removed from playlist"* (popup).  

---

## 7. Search Feature  
**Find tracks instantly**  
1. Use the **search bar** above the track list.  
2. Type any part of:  
   - Title  
   - Artist  
   - Genre  
3. Results update when you:  
   - Press **Enter**  or click the **Search button**  

---

## Troubleshooting  
- **Unexpected popups?**  
  - `"Invalid input."`: Check for typos in forms.  
  - `"Something went wrong."`: Refresh the page.  
- **Search issues?** Clear the search box and press Enter.  

---

**Enjoy your music library!** 🎵  
*Clear popups guide you through every action, and confirmations prevent accidental deletions.*  
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

### 3. Future Plans to Improve the API

- **Add statistics and analytics:** Provide insights such as the most popular tracks, playlists with the highest number of additions, and user activity summaries to enhance user experience and inform development.
- **Add search functionality in the playlists section:** Enable users to quickly find playlists by name or other criteria, improving navigation and usability.
- **Explore alternative implementations for adding tracks:** Consider different UI/UX approaches to streamline how users add tracks to playlists beyond the current method.
- **Enhance layout and design:** Improve the visual design for a cleaner, more modern, and accessible interface.
- **Standardised Data Format (Automated behind the scenes):** Implement automated data cleaning and formatting (e.g., consistent capitalization, trimming whitespace) to maintain clean, uniform database entries and prevent duplicates, all handled transparently without user intervention.

### 4. References


- **[dotenv](https://www.geeksforgeeks.org/using-python-environment-variables-with-python-dotenv/)**: Used to load environment variables from a `.env` file.  
- **[virtualenvs](https://docs.python-guide.org/dev/virtualenvs/)**: Used to set up a virtual environment.  
- **[HTML](https://www.w3schools.com/html/)**: Useful for understanding the basics of HTML.  
- **[JavaScript](https://www.w3schools.com/js/default.asp)**: Covers the basics of JavaScript.  
- **[ChatGPT](https://chatgpt.com/)** and **[DeepSeek](https://chat.deepseek.com/)**: Used to generate ideas and resolve problems throughout development. AI tools were instrumental in assisting with design strategies, debugging support, and accelerating feature creation.

These are just **sample prompts** that illustrate the approach taken to guide the implementation of various features using AI tools like ChatGPT and DeepSeek. They demonstrate the **technique of crafting prompts** for solving specific technical challenges.

---

#### Sample Prompt to realise View Tracks:

I'm building a music playlist web app using Flask and JavaScript. I want to create a feature where users can click a "View Tracks" button next to a playlist, and it should display all the tracks in that playlist using AJAX.

When the button is clicked:

- "Hide all other sections."
- "Show a new section with the playlist's name and a list of tracks (title and artist)."
- "If there are no tracks, display 'Nothing in playlist'."
- "Each track should have a 'Remove' button that deletes the track from the playlist via AJAX and removes it from the DOM."
- "If all tracks are removed, show the 'Nothing in playlist' message again."

Also include a function to go back to the main track table and restore search and button visibility. Can you help write the JavaScript?

---

#### Sample Prompt to realise Add Track

##### 1. Main Prompt for Add-to-Playlist Feature (AJAX & UI)

I'm creating a music web app using Flask and JavaScript. I want to allow users to add a track to a playlist. When a user clicks "Add to Playlist" on a track:

- It should hide the current table and show a new section with a list of existing playlists.
- Each playlist should have an "Add" button.
- When the user clicks "Add", it should send a POST request via AJAX to add the track to that playlist.
- After success, it should show a success message and return to the main track list.

Can you write the JavaScript functions to achieve this, including any helper functions like getting the track ID, rendering playlists, and switching views?

##### 2. Prompt for Just the Playlist Loader + Renderer

I need to dynamically load playlists via AJAX and render them into a table body using JavaScript. Each playlist row should include the playlist name and an "Add" button. When clicked, that button should call a function to add a track (track ID passed in) to the playlist.

Can you write a `loadPlaylists(trackId)` function that fetches the playlists and a `renderPlaylists(playlists, trackId)` function that generates the HTML?

##### 3. Prompt for Return to Track Table

After a track is added to a playlist, I want to go back to the main track list view.

Can you write a `returnToTrackList()` JavaScript function that:

- "Hides the 'Add to Playlist' view"
- "Shows the track table, search box, and top buttons"
- "Clears the search input"
- "Refreshes the track list by calling `getAll()`?"
---

