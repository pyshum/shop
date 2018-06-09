from django.urls import include, path, re_path
from shop import views


app_name = 'shop'

urlpatterns = [
    re_path(r'^$', views.ProductList, name='ProductList'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]
