from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):

    # if request.method != "PSOT":
    #   return Response({"detail": "GET not allowed"},status=405)

    instance = Product.objects.all().order_by("?").first()
    data={}
    if instance:
        # data = model_to_dict(instance, fields=["id","title","price","sale_price"])
        data= ProductSerializer(instance).data
    return Response(data)


@api_view(["POST" ])
def api_home(request, *args, **kwargs):

    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid":"not god data"},status=400)

















# def api_home(request, *args, **kwargs):

#     # print(request.GET)
#     # print(request.POST)
#     body = request.body
#     # print(body)
#     data={}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     # data["headers"] = request.headers
#     data['params'] = dict(request.GET)
    
#     data["headers"] = json.dumps(dict(request.headers))
#     data["content_type"] = request.content_type
#     # print(data)
#     return JsonResponse(data)