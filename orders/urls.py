from django.urls import path, re_path
from . import views

app_name = 'orders'

urlpatterns = [
    re_path(r'^create/$', views.OrderCreate, name='OrderCreate')
]