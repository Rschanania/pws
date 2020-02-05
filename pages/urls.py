from django.urls import path
from . import views
urlpatterns=[

path('about/',views.about,name="about"),
path('contact/',views.contact,name="contact"),
path("data/<int:id>",views.data,name="data"),
path("team/",views.team,name="team"),


]