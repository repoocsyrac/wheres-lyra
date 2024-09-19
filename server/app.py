from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient, DESCENDING
from flask_socketio import SocketIO
import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins" : "http://127.0.0.1:8080"}})
socketio = SocketIO(app, cors_allowed_origins="*")

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['wheres_lyra_db']
sightings_collection = db['sightings']
cooldown_collection = db['cooldowns']

COOLDOWN_PERIOD = 30*60 # 30 min cooldown

# Get client IP to implement cooldown
def get_client_ip():
    return request.headers.get('X-Forwarded-For', request.remote_addr)


@app.route('/')
def hello_world():
    return "hello world"

# Route to get all sightings
@app.route('/api/sightings', methods=['GET'])
@cross_origin()
def get_sightings():
    sightings = list(sightings_collection.find().sort('timestamp', DESCENDING))
    for sighting in sightings:
        sighting['_id'] = str(sighting['_id'])
    response = jsonify(sightings)
    return response

# Route to add a sighting
@app.route('/api/sightings', methods=['POST'])
@cross_origin()
def add_sighting():
    data = request.get_json()
    if 'location' not in data:
        return jsonify({"error": "Location is required"}), 400
    
    # Get client's IP
    client_ip = get_client_ip()

    # Get current time
    current_time = datetime.datetime.now()

    # Check if the user has previously reported a sighting
    last_sighting = cooldown_collection.find_one({"ip": client_ip})

    # If user has reported a sighting before, check against cooldown
    if last_sighting:
        last_sighting_time = last_sighting['last_sighting_time']
        time_since_last_sighting = (current_time - last_sighting_time).total_seconds()

        if time_since_last_sighting < COOLDOWN_PERIOD:
            time_left = COOLDOWN_PERIOD - time_since_last_sighting
            return jsonify({"error": "You are on cooldown", 
                            "time_left": time_left}), 429

    # If user has not reported a sighting before, or cooldown has passed, add new sighting
    new_sighting = {
        "location": data['location'],
        "timestamp": datetime.datetime.now()
    }
    sightings_collection.insert_one(new_sighting)

    # Emit new sighting to all connected clients
    socketio.emit('new_sighting', {"location": data['location'],
                                   "timestamp": new_sighting['timestamp'].strftime('%Y-%m-%d %H:%M:%S')})
    
    # Update users cooldown timestamp
    cooldown_collection.update_one({"ip": client_ip}, 
                                   {"$set": {"last_sighting_time": current_time}}, upsert=True)
    
    return jsonify({"message": "Sighting added!"}), 201

if __name__ == "__main__":
    app.run(debug=True)