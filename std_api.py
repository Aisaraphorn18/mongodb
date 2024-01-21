# python -u "d:\Appdev\mongodb\std.py"
import pymongo
from flask import Flask,request,jsonify,Response
import json
from bson.objectid import ObjectId

app = Flask(__name__)

uri = "mongodb+srv://merlinz:jamper2543@cluster0.mc6i7mo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = pymongo.MongoClient(uri)

# try:
#         client.admin.command("ping")
#         db = client["students"]
#         collection = db["std_info"]
#         all_students = collection.find()
#         std_id = '6130300654'
#         print(collection.find_one({"_id":std_id}))
#         # for std in all_students:
#         #         print(std)
#         # return Response(
#         #     response = {all_students},
#         #     status = 200 ,
#         #     mimetype = "application/json"
#         # )
# except Exception as e:
#         print("Can't Find")

@app.route("/",methods = ["GET"])
def get_index():
    try:
        client.admin.command("ping")
        return("Welcome  to Students Management API")
    except Exception as e:
        print(e)

@app.route("/students/",methods = ["GET"])
def get_students():
    try:
        client.admin.command("ping")
        db = client["students"]
        collection = db["std_info"]
        get_all_students = list(collection.find())
        # data = list(all_students)
        return Response (
            response = json.dumps(get_all_students),
            status = 200 ,
            mimetype = "application/json"
        )
    except Exception as e:
        print(e)

@app.route("/students/<int:std_id>",methods = ["GET"])
def get_students2(std_id):
    try:
        client.admin.command("ping")
        db = client["students"]
        collection = db["std_info"]
        std_id2 = str(std_id)
        # print(std_id2)
        get_students = collection.find_one({"_id":std_id2})
        print(get_students)
        # data = list(all_students)
        # return Response (
        #         response = json.dumps(get_students),
        #         status = 200 ,
        #         mimetype = "application/json"
        #     )
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
    # except Exception as e:
    #     # error_code =
    #     return Response (
    #         response = json.dumps({"error":"Student not found"}),
    #         status = 404 ,
    #         mimetype = "application/json"
    #     )
    except Exception as e:
        print(e)



if __name__ == "__main__" :
        app.run(debug=True, port=5001, host='0.0.0.0')

# Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
#     db = client["students"]
#     collection = db["std_info"]
#     while True:
#         print("===MENU===")
#         print("1: show all records")
#         print("2: insert record")
#         print("3: update record")
#         print("4: delete record")
#         print("5: exit")
#         choice = input("Please choose:")
#         choice = int(choice)
#         if choice == 1:
#             print(f"found {collection.count_documents({})} records")
#             all_students = collection.find()
#             for std in all_students:
#                 print(std)
#         elif choice == 2:
#             id = input("Input student id:")
#             name = input("Input fullname:")
#             major = input("Input major:")
#             gpa = input("Input gpa:")
#             gpa = float(gpa)
#             try:
#                 collection.insert_one(
#                     {"_id": id, "fullname": name, "major": major, "gpa": gpa}
#                 )
#             except Exception as e:
#                 print(e)
#         elif choice == 3:
#             id_to_update = input("Input student id to update:")
#             new_gpa = float(input("Input new gpa:"))
#             try:
#                 collection.update_one({"_id": id_to_update}, {"$set": {"gpa": new_gpa}})
#                 print("Record updated successfully.")
#             except Exception as e:
#                 print(e)
#         elif choice == 4:
#             id_to_delete = input("Input student id to delete:")
#             try:
#                 collection.delete_one({"_id": id_to_delete})
#                 print("Record deleted successfully.")
#             except Exception as e:
#                 print(e)
#         elif choice == 5:
#             break

# except Exception as e:
#     print(e)
# finally:
#     client.close()

