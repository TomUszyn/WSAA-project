from flask import Flask, jsonify, request, abort, render_template
from playlistsDAO import PlaylistsDAO
from datetime import datetime


app = Flask(__name__)
dao = PlaylistsDAO()

# The index route serves the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Get all tracks
@app.route('/api/tracks', methods=['GET'])
def get_all_tracks():
    try:
        tracks = dao.getAll()
        return jsonify(tracks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get track by ID
@app.route('/api/tracks/<int:track_id>', methods=['GET'])
def get_track(track_id):
    try:
        track = dao.findByID(track_id)
        if track:
            return jsonify(track)
        else:
            return jsonify({"error": "Track not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Create a new track
@app.route('/api/tracks', methods=['POST'])
def create_track():
    try:
        data = request.get_json()
        if not data or "title" not in data or "artist" not in data:
            return jsonify({"error": "Missing 'title' or 'artist'"}), 400
        new_track = dao.createTrack(data)
        return jsonify(new_track), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Update track
@app.route('/api/tracks/<int:track_id>', methods=['PUT'])
def update_track(track_id):
    try:
        data = request.get_json()
        updated = dao.update(track_id, data)
        return jsonify(updated)
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

 # Delete track
@app.route('/api/tracks/<int:track_id>', methods=['DELETE'])
def delete_track(track_id):
    try:
        result = dao.delete(track_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Get all playlists
@app.route('/api/playlists', methods=['GET'])
def show_playlists():
    try:
        playlists = dao.getAllPlaylists()
        return jsonify(playlists)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
 # Create a new playlist   
@app.route('/api/playlists', methods=['POST'])
def create_playlist():
    try:
        data = request.get_json()
        new_playlist = dao.createPlaylist(data)
        return jsonify(new_playlist), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update Playlist
@app.route('/api/playlists/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    try:
        data = request.get_json()
        if 'name' not in data:
            return jsonify({"error": "'name' field is required"}), 400
        updated_playlist = dao.updatePlaylistName(playlist_id, data['name'])
        return jsonify(updated_playlist)
    except ValueError as e:
        return jsonify({"error": str(e)}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Playlist by ID
@app.route('/api/playlists/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    try:
        playlist = dao.findPlaylistByID(playlist_id)  # Update this method if necessary
        if playlist:
            return jsonify(playlist)
        else:
            return jsonify({"error": "Playlist not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete Playlist
@app.route('/api/playlists/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    try:
        result = dao.deletePlaylistByID(playlist_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__' :
    app.run(debug= True)
