from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



@login_required
def place_list(request):

    if request.method == 'POST':
        # create new place
        form = NewPlaceForm(request.POST) # creating a new instance of the NewPlaceForm instead of creating new empty form, which i think is more code
        place = form.save(commit=False) # save the new place to the database
        place.user = request.user
        if form.is_valid(): # validation against DB constraints
            place.save() # save the new place to the database
            return redirect('place_list') # reloads the homepage

    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name') # get all the places from the database, and store them in a variable called places
    new_place_form = NewPlaceForm() # create a new instance of the NewPlaceForm, and store it in a variable called new_place_form
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form}) 

@login_required
def about(request):
    author = 'Jacob Zapp'
    about = 'This is a wishlist of places I want to visit, and places I have already been to.'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})

@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True).order_by('name') # get all the places from the database, and store them in a variable called visited
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':

       # place = Place.objects.get(pk=place_pk) # get the place from the database that matches the primary key that was passed in the URL
        place = get_object_or_404(Place, pk=place_pk) # get the place from the database that matches the primary key that was passed in the URL, and if it doesn't exist, return a 404 error
        if place.user == request.uder:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden

    return redirect('place_list')   


@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)

    return render(request, 'travel_wishlist/place_detail.html', {'place': place})