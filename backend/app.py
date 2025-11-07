import json
from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

app = Flask(__name__)

client =  pymongo.MongoClient(os.getenv("MONGODB_URI"))
db = client.test
collection = db['tuteDudeUsers']

@app.route('/api', methods=['GET'])
def get_data():
    with open('./data/api.json', 'r') as f:
        data_list = json.load(f)
    
    return jsonify(data_list)

@app.route('/submit', methods=['POST'])
def post_data(): 
    try:
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({"status": True}), 200
    except Exception as e:
        return jsonify({"status": False, "error": str(e)}), 500
    

if __name__ == '__main__':
    # You might want to change the port or use a WSGI server for production
    app.run(host="0.0.0.0", port=5000, debug=True)