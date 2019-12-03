from django.http import HttpResponse
import json

def index(request):
    return HttpResponse("Hello, world. You're at the user index")

def fetch(request,user_name):
    # print(request.body)
    payload = json.loads(request.body)
    print(payload["name"])
    return HttpResponse("Hello, world. You're at the polls index. %s" %user_name)

