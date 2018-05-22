#####packages#####

from pymongo import MongoClient

#####end-packages#####

#credentials
host = "localhost"
port = 27017
db = "customer"

def connect(): #this method can be used to establish a connection with database
    try:
        mongo_connection = MongoClient(host + ":" + str(port))
        mongo_database = mongo_connection[db]
        return mongo_database
    except Exception as e:
        pass

database = connect()

def get_db(): #this method returns the database
    temp_list = []
    result = database.customer_info.find({})
    for cur in result:
        cur["_id"] = str(cur["_id"])
        temp_list.append(cur)
    print temp_list
    return temp_list


# not yet used

# def get_latest():
#     #write the logic to add only latest element
#     temp_list = []
#     temp_list = database.customer_info.find().sort({"_id" : -1}).limit(1)
#     value = None
#     for cur in temp_list:
#         value = cur
#     return value

# not used #

# def show_results(request):
#     try:
#         li = get_db()
#         if request.method == "POST":
#             return dumps(li)
#         else:
#             pass
#     except Exception as e:
#         print e
