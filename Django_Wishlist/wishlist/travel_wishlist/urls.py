from django.urls import path # import the path function from the django.urls module, which we will use to define URL patterns for our app   
from . import views # import the views file from the current directory, so we can use the functions in it to handle requests

urlpatterns = [
    path('', views.place_list, name='place_list'), 
    path('visited', views.places_visited, name='places_visited'), # visited page
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'), # mark a place as visited
    path('place/<int:place_pk>', views.place_details, name='place_details'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place'),
    path('about', views.about, name='about') # about page
]