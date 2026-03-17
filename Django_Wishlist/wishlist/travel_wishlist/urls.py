from django.urls import path # import the path function from the django.urls module, which we will use to define URL patterns for our app   
from . import views # import the views file from the current directory, so we can use the functions in it to handle requests

urlpatterns = [
    path('', views.place_list, name='place_list'), 
]