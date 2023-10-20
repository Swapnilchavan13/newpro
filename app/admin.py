from django.contrib import admin
from .models import *

# Register your models here.




class ImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Images._meta.fields]

admin.site.register(Images,ImageAdmin)
