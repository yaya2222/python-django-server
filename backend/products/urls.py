from django.urls import path

from . import views

urlpatterns = [
    path("",views.product_list_create_view),
    path("<int:pk>/",views.product_detail_view),
    path("<int:pk>/update/",views.product_updata_view),
    path("<int:pk>/delete/",views.product_detail_view),
]