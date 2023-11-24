from django.contrib import admin
from .models import *
from .forms import *


# Register your models here.

class BuildingAdmin(admin.ModelAdmin):
    form = BuildingForm

admin.site.register(Building, BuildingAdmin)
admin.site.register(Enclosure)