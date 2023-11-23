import json
from django.forms.models import  model_to_dict
from django.http import JsonResponse,HttpResponse
from django.apps import  apps
Product = apps.get_model('products', 'Product')

def api_home(request,*args,**kwargs):
    global json_data_str
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        json_data_str = json.dumps(data)
    return HttpResponse(json_data_str,headers={"content-type": "application/json"})