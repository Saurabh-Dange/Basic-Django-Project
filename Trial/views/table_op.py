######packages#####


from django.shortcuts import render
from dbcon import connect,get_db
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson.json_util import dumps
import bson
from bson.objectid import ObjectId


######end-packages#####

database = connect()

@csrf_exempt
def delete(request): # this method is used for deleting the entry from the databse using object id
    try:

        if request.method == 'POST':
            action = request.POST.get("action",None)
            if action == 'delete':
                customer_dict1 = dict()
                request_body = request.POST
                customer_dict1["_id"] = request_body.get("oid")
                database.customer_info.remove({"_id": ObjectId(customer_dict1["_id"])})
                return HttpResponse(request)

            else:
                return HttpResponse("wrong logic")
                # customer_dict = dict()
                # request_body = request.POST
                # customer_dict["name"] = request_body.get("Name")
                # customer_dict["Mobile_num"] = request_body.get("Mobile_num")
                # customer_dict["Gender"] = request_body.get("Gender")
                # result = database.customer_info.insert(customer_dict)
                # result = str(result)
                # return HttpResponse(dumps({"_id":result,"name" : customer_dict['name'], "Mobile_num" : customer_dict['Mobile_num'],
                #                            "Gender" : customer_dict['Gender']}), content_type='application/json')
        else:
            result = get_db()
            print result
            return render(request, 'dashboard/register.html', {"result": result})
        return render(request, 'dashboard/register.html')
    except Exception as e :
            return HttpResponse("failed")


@csrf_exempt
def get_entry(request): # this method returns specific entry using the object id from database
    try:

        if request.method == 'POST':
            action = request.POST.get("action",None)
            if action == 'get_entry':
                li = ()
                customer_dict1 = dict()
                request_body = request.POST
                customer_dict1["_id"] = request_body.get("oid")
                li = database.customer_info.find({"_id": ObjectId(customer_dict1["_id"])})
                return HttpResponse(dumps(li),content_type='application/json')

            else:
                return HttpResponse("wrong logic")
                # customer_dict = dict()
                # request_body = request.POST
                # customer_dict["name"] = request_body.get("Name")
                # customer_dict["Mobile_num"] = request_body.get("Mobile_num")
                # customer_dict["Gender"] = request_body.get("Gender")
                # result = database.customer_info.insert(customer_dict)
                # result = str(result)
                # return HttpResponse(dumps({"_id":result,"name" : customer_dict['name'], "Mobile_num" : customer_dict['Mobile_num'],
                #                            "Gender" : customer_dict['Gender']}), content_type='application/json')
        else:
            result = get_db()
            print result
            return render(request, 'dashboard/register.html', {"result": result})
        return render(request, 'dashboard/register.html')
    except Exception as e :
            return HttpResponse("failed")

@csrf_exempt
def update(request): #this method updates the entry in database using the object id
    try:

        if request.method == 'POST':
                customer_dict1 = dict()
                request_body = request.POST
                customer_dict1["_id"] = request_body.get("_id")
                customer_dict1["name"] = request_body.get("Name")
                customer_dict1["Mobile_num"] = request_body.get("Mobile_num")
                customer_dict1["Gender"] = request_body.get("Gender")
                result = database.customer_info.update({"_id": ObjectId(customer_dict1["_id"])},
                                              {"$set":{"name":customer_dict1["name"],"Mobile_num":customer_dict1["Mobile_num"],
                                                    "Gender":customer_dict1["Gender"]}})
                return HttpResponse("successfully updated")

                # customer_dict = dict()
                # request_body = request.POST

                # result = database.customer_info.insert(customer_dict)
                # result = str(result)
                # return HttpResponse(dumps({"_id":result,"name" : customer_dict['name'], "Mobile_num" : customer_dict['Mobile_num'],
                #                            "Gender" : customer_dict['Gender']}), content_type='application/json')
        else:
            result = get_db()
            print result
            return render(request, 'dashboard/register.html', {"result": result})
        return render(request, 'dashboard/register.html')
    except Exception as e :
            return HttpResponse("failed")