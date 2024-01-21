# python -u "d:\Appdev\mongodb\std.py"
import pymongo
from flask import Flask,request,jsonify,Response
import json
from bson.objectid import ObjectId
from flask_basicauth import BasicAuth

app = Flask(__name__)

uri = "mongodb+srv://merlinz:jamper2543@cluster0.mc6i7mo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = pymongo.MongoClient(uri)

# Auth
app.config['BASIC_AUTH_USERNAME'] = 'Merlinz'
app.config['BASIC_AUTH_PASSWORD'] = '1234toei'
basic_auth = BasicAuth(app)

@app.route("/",methods = ["GET"])
def get_index():
    try:
        client.admin.command("ping")
        return("Welcome  to Students Management API")
    except Exception as e:
        print(e)

@app.route("/students/",methods = ["GET"])
@basic_auth.required
def get_students():
    try:
        client.admin.command("ping")
        db = client["students"]
        collection = db["std_info"]
        # get_all_students = collection.find()
        get_all_students = list(collection.find())
        # data = list(all_students)
        # return jsonify({"Students":get_all_students})
        return Response (
            response = json.dumps(get_all_students),
            # response = jsonify({"Students":get_all_students}),
            status = 200 ,
            mimetype = "application/json"
        )
    except Exception as e:
        print(e)

@app.route("/students/<int:std_id>",methods = ["GET"])
@basic_auth.required
def get_students2(std_id):
    try:
        client.admin.command("ping")
        db = client["students"]
        collection = db["std_info"]
        std_id2 = str(std_id)
        # print(std_id2)
        get_students = collection.find_one({"_id":std_id2})
        # print(get_students)s
        if(get_students != None) :
            return Response (
                response = json.dumps(get_students),
                status = 200 ,
                mimetype = "application/json"
            )
        else :
            return Response (
            response = json.dumps({"error":"Student not found"}),
            status = 404 ,
            mimetype = "application/json"
            )
    except Exception as e:
        print(e)



if __name__ == "__main__" :
        app.run(debug=True, port=5001, host='0.0.0.0')
