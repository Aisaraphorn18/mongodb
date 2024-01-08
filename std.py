# python -u "d:\Appdev\mongodb\std.py"
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kibbi:Kifkif2547!@cluster0.mc6i7mo.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["students"]
    collection = db["std_info"]
    while True:
        print("===MENU===")
        print("1: show all records")
        print("2: insert record")
        print("3: update record")
        print("4: delete record")
        print("5: exit")
        choice = input("Please choose:")
        choice = int(choice)
        if choice == 1:
            print(f"found {collection.count_documents({})} records")
            all_students = collection.find()
            for std in all_students:
                print(std)
        elif choice == 2:
            id = input("Input student id:")
            name = input("Input fullname:")
            major = input("Input major:")
            gpa = input("Input gpa:")
            gpa = float(gpa)
            try:
                collection.insert_one(
                    {"_id": id, "fullname": name, "major": major, "gpa": gpa}
                )
            except Exception as e:
                print(e)
        elif choice == 3:
            id_to_update = input("Input student id to update:")
            new_gpa = float(input("Input new gpa:"))
            try:
                collection.update_one({"_id": id_to_update}, {"$set": {"gpa": new_gpa}})
                print("Record updated successfully.")
            except Exception as e:
                print(e)
        elif choice == 4:
            id_to_delete = input("Input student id to delete:")
            try:
                collection.delete_one({"_id": id_to_delete})
                print("Record deleted successfully.")
            except Exception as e:
                print(e)
        elif choice == 5:
            break

except Exception as e:
    print(e)
finally:
    client.close()

