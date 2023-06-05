from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer



# קבלת מוצר לפי id
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"

product_detail_view=ProductDetailAPIView.as_view()


# קבלת מוצר לפי id
class ProductUpdataAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title



product_updata_view=ProductUpdataAPIView.as_view()


# יצירת מוצר / קבלת כל המוצרים
class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # המידע שהגיע בבקשה
        # print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        if content is None:
            content=title
        serializer.save(content=content)

product_list_create_view=ProductListCreateApiView.as_view()


# # קבלת כל המוצרים
# class ProductListAPIView(generics.ListAPIView):
#     """
#     אין צורך בשימוש כיון שבבקשת 
#     create list 
#     אם אני מקבל חזרה את כל הרשימה
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = "pk"

# product_list_view=ProductListAPIView.as_view()


# # יצירת מוצר
# class ProductCreateApiView(generics.CreateAPIView):
#     queryset=Product.objects.all()
#     serializer_class = ProductSerializer

#     def perform_create(self, serializer):
#         # המידע שהגיע בבקשה
#         # print(serializer.validated_data)
#         title=serializer.validated_data.get("title")
#         content=serializer.validated_data.get("content")
#         if content is None:
#             content=title
#         serializer.save(content=content)

# product_create_view=ProductCreateApiView.as_view()