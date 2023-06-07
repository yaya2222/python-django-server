from rest_framework import generics,mixins #, permissions, authentication

# from api.authentication import TokenAuthentication

from .models import Product
from .serializers import ProductSerializer
# from api.permissions import IsStaffEditorPermission
from api.mixins import  StaffEditorPermissionMixin



# קבלת מוצר לפי id
class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = 

    # lookup_field = "pk"

product_detail_view=ProductDetailAPIView.as_view()


# עידכון מוצר לפי id
class ProductUpdataAPIView(
    StaffEditorPermissionMixin ,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title

product_updata_view=ProductUpdataAPIView.as_view()


# מחיקת מוצר לפי id
class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self,instance):

        super().perform_destroy(instance)


product_destroy_view=ProductDestroyAPIView.as_view()


# יצירת מוצר / קבלת כל המוצרים
class ProductListCreateApiView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
    # permission_classes = [ permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self, serializer):
        # המידע שהגיע בבקשה
        # print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        if content is None:
            content=title
        serializer.save(content=content)

product_list_create_view=ProductListCreateApiView.as_view()

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field= "pk"

    def get(self,request,*args,**kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def perform_create(self, serializer):
        # המידע שהגיע בבקשה
        # print(serializer.validated_data)
        title=serializer.validated_data.get("title")
        content=serializer.validated_data.get("content")
        if content is None:
            content="bla bla"
        serializer.save(content=content)

product_mixin_view=ProductMixinView.as_view()

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