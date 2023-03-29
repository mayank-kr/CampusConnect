from django.urls import path

from . import views

urlpatterns = [
    path('importantContacts/emergency/', views.emergency, name='emergency'),
    path('importantContacts/administration/',
         views.administration, name='administration'),
    path('importantContacts/faculty/', views.faculty, name='faculty'),
    path('profile/', views.profile, name='profile'),
]
