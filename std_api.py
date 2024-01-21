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

@app.route("/students",methods = ["GET","POST"])
@basic_auth.required
def students():
    try :
        client.admin.command("ping")
        db = client["students"]
        collection = db["std_info"]
        if (request.method  == "GET" ) :
            try:
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
        if (request.method  == "POST" ) :
            try:
                data = request.get_json()
                new_student = {
                    "_id" : data["_id"],
                    "fullname" : data["fullname"],
                    "major" : data["major"],
                    "gpa" : data["gpa"]
                }

                dbResponse = collection.insert_one(new_student)
                # print(insert)
                # print("insert Result : ")
                # print(dbResponse)
                # return new_student
                return Response (
                    response = json.dumps({"_id" : data["_id"],"fullname" : data["fullname"],"major" : data["major"],"gpa" : data["gpa"]}) ,
                    # response = json.dumps({"_id" : data["_id"],"fullname" : data["fullname"],"major" : data["major"],"gpa" : data["gpa"]}) ,
                    status = 200 ,
                    mimetype = "application/json"
                    )
            # collection.insert_one(new_student)
            except Exception as e:
                print(e)
                return Response (
                        response = json.dumps({"error":"Cannot create new student"}),
                        status = 500 ,
                        mimetype = "application/json"
                        )
    except Exception as e : 
        print(e)
        return Response (
        response = json.dumps({"error":"Cannot Connect DB"}),
        status = 404 ,
        mimetype = "application/json"
        )


@app.route("/students/<int:std_id>",methods = ["GET","PUT","DELETE"])
@basic_auth.required
def students2(std_id):
    try :
        client.admin.command("ping")
        db = client["students"]
        collection = db["std_info"]
        if(request.method == "GET") :
            try:
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
                return Response (
                    response = json.dumps({"error":"Student not found"}),
                    status = 404 ,
                    mimetype = "application/json"
                    )
        if(request.method == "PUT") :
            try :
                # print("Test PUT")
                std_id2 = str(std_id)
                get_students = collection.find_one({"_id":std_id2})
                # print(get_students)
                # get_id = next((b for b in get_students if b["_id"]==std_id),None)
                # print(get_students["_id"])
                # if get_id:
                if (get_students["_id"] == std_id2):
                    data = request.get_json()
                    # get_students.update(data)
                    collection.update_one({"_id" : data["_id"] if data["_id"] in std_id2 else data["_id"]},{"$set":{"fullname" : data["fullname"],"major" : data["major"],"gpa" : data["gpa"]}})
                    get_students = collection.find_one({"_id":std_id2})
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
            except Exception as e :
                print(e)
                return Response (
                    response = json.dumps({"error":"Student not found"}),
                    status = 404 ,
                    mimetype = "application/json"
                    )
        if(request.method == "DELETE") :
            try :
                std_id2 = str(std_id)
                get_students = collection.find_one({"_id":std_id2})
                # print("Test DELETE")
                # get_id = next((b for b in get_students if b["_id"]==std_id),None)
                if (get_students["_id"] == std_id2):
                    delete_student =  collection.delete_one({"_id":std_id2})
                    return Response (
                        response = json.dumps({"message":"Student deleted scessfullyuc"}),
                        status = 200 ,
                        mimetype = "application/json"
                    )
            except Exception as e :
                print(e)
                return Response (
                    response = json.dumps({"error":"Student not found"}),
                    status = 404 ,
                    mimetype = "application/json"
                    )
    except Exception as e :
        print(e)
        return Response (
        response = json.dumps({"error":"Cannot Connect DB"}),
        status = 404 ,
        mimetype = "application/json"
        )

if (__name__ == "__main__") :
    app.run(debug=True, port=5001, host='0.0.0.0')

# @app.route("/students",methods = ["POST"])
# # @basic_auth.required
# def post_students():
#     try:
#         client.admin.command("ping")
#         db = client["students"]
#         collection = db["std_info"]
#         data = request.get_json()
#         new_student = {
#             "_id" : data["_id"],
#             "fullname" : data["fullname"],
#             "major" : data["major"],
#             "gpa" : data["gpa"]
#         }

#         dbResponse = collection.insert_one(new_student)
#         # print(insert)
#         print("insert Result : ")
#         print(dbResponse)
#         # return new_student
#         return Response (
#             response = json.dumps({"_id" : data["_id"],"fullname" : data["fullname"],"major" : data["major"],"gpa" : data["gpa"]}) ,
#             # response = json.dumps({"_id" : data["_id"],"fullname" : data["fullname"],"major" : data["major"],"gpa" : data["gpa"]}) ,
#             status = 200 ,
#             mimetype = "application/json"
#             )
#         # collection.insert_one(new_student)
#     except Exception as e:
#         print(e)
#         return Response (
#                 response = json.dumps({"error":"Cannot create new student"}),
#                 status = 500 ,
#                 mimetype = "application/json"
#                 )




