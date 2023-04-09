from django.contrib import admin

# Register your models here.
from .models import Contact, Users, Sell, Buy, Lost, Found, CabSharing, Mess, Restaurants, Todo

admin.site.register(Contact)
admin.site.register(Users)
admin.site.register(Sell)
admin.site.register(Buy)
admin.site.register(Lost)
admin.site.register(Found)
admin.site.register(CabSharing)
admin.site.register(Mess)
admin.site.register(Restaurants)
admin.site.register(Todo)
