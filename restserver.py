from flask import Flask, jsonify, request, abort
from playlistsDAO import PlaylistsDAO
from datetime import datetime

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/tracks')
def getAll():
    #print("in getall")
    results = PlaylistsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"

@app.route('/tracks/<int:id>')
def findById(id):
    foundTrack = PlaylistsDAO.findByID(id)

    if not foundTrack:  # Check if the track doesn't exist
        # Return a 404 status with a structured error response
        error_response = {
            "error": {
                "code": "TRACK_NOT_FOUND",
                "message": f"The track with ID {id} does not exist.",
                "status": 404,
                "timestamp": datetime.utcnow().isoformat()  # Current UTC timestamp
            }
        }
        return jsonify(error_response), 404

    return jsonify(foundTrack)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books

@app.route('/tracks', methods=['POST'])
def createTrack():
    if not request.json:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    # Get values from the request, and set default values if missing
    title = request.json.get('title')  # title is mandatory
    artist = request.json.get('artist')  # artist is mandatory
    genre = request.json.get('genre', None)  # genre is optional, default to None if not provided
    play_count = request.json.get('play_count', None)  # play_count is optional, default to None if not provided
    listeners = request.json.get('listeners', None)  # listeners is optional, default to None if not provided
    
    # Basic validation to ensure title and artist are provided
    if not title or not artist:
        return jsonify({"error": "Title and artist are required"}), 400

    # Construct track dictionary
    track = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "play_count": play_count,
        "listeners": listeners
    }
    
    # Call DAO to insert the track
    addedTrack = PlaylistsDAO.createTrack(track)
    
    # Return the added track as a response
    return jsonify(addedTrack), 201

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"Someone like you\",\"artist\":\"Adele\",\"genre\":pop}" http://127.0.0.1:5000/books/1

@app.route('/tracks/<int:id>', methods=['PUT'])
def update(id):
    foundTrack = PlaylistsDAO.findByID(id)
    if not foundTrack:
        abort(404)

    if not request.json:
        abort(400)
    
    reqJson = request.json

    # Validate play_count and listeners (if present in the request)
    if 'play_count' in reqJson and type(reqJson['play_count']) is not int:
        abort(400)
    if 'listeners' in reqJson and type(reqJson['listeners']) is not int:
        abort(400)

    # Update foundTrack with request data
    if 'title' in reqJson:
        foundTrack['title'] = reqJson['title']
    if 'artist' in reqJson:
        foundTrack['artist'] = reqJson['artist']
    if 'genre' in reqJson:
        foundTrack['genre'] = reqJson['genre']
    if 'play_count' in reqJson:
        foundTrack['play_count'] = reqJson['play_count']
    if 'listeners' in reqJson:
        foundTrack['listeners'] = reqJson['listeners']

    # Now call the DAO update method
    updated_track = PlaylistsDAO.update(id, foundTrack)

    # If the update is successful, return the updated track
    if updated_track:
        return jsonify(updated_track), 200  # Return the updated track with a success status
    else:
        return jsonify({"error": "Failed to update track"}), 400  # Error if update failed
        
@app.route('/tracks/<int:id>', methods=['DELETE'])
def delete(id):
    # Check if the track exists before attempting to delete
    foundTrack = PlaylistsDAO.findByID(id)
    
    if not foundTrack:
        # If the track does not exist, return a 404 status with a structured error response
        error_response = {
            "error": {
                "code": "TRACK_NOT_FOUND",
                "message": f"The track with ID {id} does not exist.",
                "status": 404,
                "timestamp": datetime.utcnow().isoformat()  # Current UTC timestamp
            }
        }
        return jsonify(error_response), 404

    # If the track exists, proceed with deletion
    PlaylistsDAO.delete(id)
    
    # Return a success message
    return jsonify({"done": True}), 200    

#@app.route('/playlists/<int:id>' , methods=['DELETE'])
#def delete(id):
#    PlaylistsDAO.delete(id)
#    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)
