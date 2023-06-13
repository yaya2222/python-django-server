from rest_framework import serializers
from rest_framework.reverse import reverse 

from .models import Product
from .validators import validate_title_no_hello ,unique_product_title
from api.serializers import UserPublicSerializer



class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk",read_only=True)
    title = serializers.CharField(read_only=True)




class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer( source="user",read_only = True)
    related_products = ProductInlineSerializer(source="user.product_set.all",read_only=True, many=True)
    
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail",lookup_field="pk")
    title = serializers.CharField(validators=[validate_title_no_hello,unique_product_title])
    # name = serializers.CharField(source="title", read_only=True)
    # email = serializers.EmailField(source="user.email",read_only=True)
    class Meta:
        model = Product
        fields = [
            "owner", 
            # "email",
            "edit_url",
            'url',
            "pk",
            "title",
            # "name",
            "content",
            "price",
            "sale_price",
            "my_discount",
            "related_products",
            "my_user_data",
        ]

    def get_my_user_data(self , obj):
        # print("------------------")
        # print(self)
        # print(obj)
        return{
            "username":obj.user.username
        }

#   כהה בודקים תנאים
#   def validate_<name field>
    # def validate_title(self, value):
    #     request = self.context.get("request")
    #     user = request.user
    #     qs = Product.objects.filter(user=user,title__iexact=value)
    #     if (qs.exists()):
    #         raise serializers.ValidationError(f"{value} is already exsit")
    #     return value
    

    # def create(self, validated_data):
    #     # email=validated_data.pop("email")
    #     obj= super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     instance.title=validated_data.get("title")
    #     return instance

    def get_my_discount(self,obj):
        if not hasattr(obj,"id"):
            return None
        
        if not isinstance(obj,Product):
            return None
        
        return obj.get_discount()
    
    # def get_url(self,obj):
    #     # return f"/api/products/{obj.pk}/"
     #     if request is None:
    #         return None
    #     return reverse("product-detail",kwargs={"pk":obj.pk},request=request )
    
    def get_edit_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request )

     