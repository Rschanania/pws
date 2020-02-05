from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('contact/',views.contact,name='Contact'),
    path('edit/',views.edit,name="edit"),
    path('index/',views.index,name="index"),
]