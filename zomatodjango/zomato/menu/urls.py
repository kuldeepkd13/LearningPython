from django.urls import path
from menu import views

urlpatterns = [
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add', views.add_dish, name='add_dish'),
    path('menu/remove/<str:dishId>/', views.remove_dish, name='remove_dish'),
    path('menu/update/<str:dishId>/', views.update_dish, name='update_dish'),
    path('order/', views.order_list, name='order_list'),
    path('order/takeorder', views.take_order, name='take_order'),
    path('order/UpdateStatus/<int:OrderId>', views.update_order_status, name='update_order_status'),
    path('order/filter/<str:status>', views.filter , name='filter')

]