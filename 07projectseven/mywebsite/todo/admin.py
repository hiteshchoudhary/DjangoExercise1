from django.contrib import admin

# Register your models here.

from .models import Todo

admin.site.register(Todo)
