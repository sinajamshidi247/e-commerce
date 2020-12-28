from django.urls import path
from . import views




app_name = 'shop'

urlpatterns = [
    path('',views.Home,name='home'),
    path('category/<slug:slug>/',views.Home,name='category_filter'),
    path('<slug:slug>/',views.product_detail,name='product_detail')

]