from django.urls import path 
from. import views


app_name = 'cart'


urlpatterns = [
   
    path('',views.detail,name = 'detail'),
    path('add/<int:product_id>',views.AddCart,name = 'addcart'),
    path('remove/<int:product_id>',views.RemoveCart,name = 'removecart'),


]