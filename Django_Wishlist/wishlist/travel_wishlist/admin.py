from django.contrib import admin
from .models import Place

# Register your models here.
admin.site.register(Place) # registering the model we made so we can see it in the admin interface, and add data to it from there.

