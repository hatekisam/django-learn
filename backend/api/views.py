import json

from django.http import  JsonResponse

def api_home(request,*args,**kwargs):
    body = request.body
    print(body)
    data={}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse(data)