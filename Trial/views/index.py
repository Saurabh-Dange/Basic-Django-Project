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

#this establishes connection with database
database = connect()


#  this method is linked with the front index page which simply displayes the welcome page
def index(request):
    return render(request, 'dashboard/index.html')


# this method is linked with the registration page which gets the data from input field
# and then stores it in a database
@csrf_exempt
def register(request):

    try:

        if request.method == 'POST':
            action = request.POST.get("action", None)
            if action == 'delete': # this part of code is redundant there is different method for deleting record
                customer_dict1 = dict()
                request_body = request.POST
                customer_dict1["_id"] = request_body.get("oid")
                database.customer_info.remove({"_id": ObjectId(customer_dict1["_id"])})
                return HttpResponse("deleted")

            customer_dict = dict() #main part of register method starts here
            request_body = request.POST
            customer_dict["name"] = request_body.get("Name")
            customer_dict["Mobile_num"] = request_body.get("Mobile_num")
            customer_dict["Gender"] = request_body.get("Gender")
            result = database.customer_info.insert(customer_dict) #gets the details of customer from front end and then
                                                                  #it is stored in the database
            result = str(result) #redundant line of code
            return HttpResponse(dumps(customer_dict), content_type='application/json')
        else:
            result = get_db() #this part of code is not used there's different method "display" to do this
            print result
            return render(request, 'dashboard/register.html', {"result": result})
        return render(request, 'dashboard/register.html')
    except Exception as e :
            return HttpResponse("failed")


@csrf_exempt
def display(request): #it passes all the data from database in form of the list in JSON form
    try:
        if request.method == 'POST':
            li = get_db()
            return HttpResponse(dumps(li), content_type='application/json')

    except Exception as e :
            return HttpResponse("failed")
