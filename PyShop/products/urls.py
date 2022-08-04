from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_products),
    path('old/page', views.old_product_page)
]