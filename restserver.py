from flask import Flask, jsonify, request, abort
from playlistsDAO import PlaylistsDAO
from datetime import datetime




app = Flask(__name__)
dao = PlaylistsDAO()


@app.route('/')
def index():
    return "Hello, World!"


# Get all tracks
@app.route('/tracks', methods=['GET'])
def get_all_tracks():
    try:
        tracks = dao.getAll()
        return jsonify(tracks)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get track by ID
@app.route('/tracks/<int:track_id>', methods=['GET'])
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
@app.route('/tracks', methods=['POST'])
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
        return jsonify({"error": str(e)}), 500


# Update track
@app.route('/tracks/<int:track_id>', methods=['PUT'])
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
@app.route('/tracks/<int:track_id>', methods=['DELETE'])
def delete_track(track_id):
    try:
        result = dao.delete(track_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__' :
    app.run(debug= True)
