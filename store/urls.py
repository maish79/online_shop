from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
   path('', views.index),
   path('items/', views.items),
   path('items/<int:id>', views.item_detail, name='item_detail'),
]