from django.urls import path
from . import views
urlpatterns = [
path('' , views.home , name='home'),
path('product/<int:product_id>' ,views.choose_pro , name='choose_pro'),
path('order_done' ,views.order_done , name='order_done'),
path('admin/orders' ,views.order_admin , name='order_admin'),
path('about',views.about,name='about'),
]