from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trix', views.get_hfaz, name='hfaz_kidz'),
]
