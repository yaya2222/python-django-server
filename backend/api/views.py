from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):

    body = request.body
    data={}
    try:
        data = json.load(body)
    except:
        pass
    print(data)
    return JsonResponse({"msg":"helllo"})