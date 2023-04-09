from django.contrib import admin

# Register your models here.
from .models import Contact, Users, Sell, Buy, Lost, Found

admin.site.register(Contact)
admin.site.register(Users)
admin.site.register(Sell)
admin.site.register(Buy)
admin.site.register(Lost)
admin.site.register(Found)