from django.contrib import admin

# Register your models here.
from .models import MyClient, ClientFiles

admin.site.register(MyClient)
admin.site.register(ClientFiles)

