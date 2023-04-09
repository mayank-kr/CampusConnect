from django.urls import path
from . import views

urlpatterns = [
    path('importantContacts/emergency/', views.emergency, name='emergency'),
    path('importantContacts/administration/',
         views.administration, name='administration'),
    path('importantContacts/faculty/', views.faculty, name='faculty'),
    path('profile', views.profile, name='profile'),
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),
    path('lostfound/lost', views.lost, name='lost'),
    path('lostfound/lost/lostform', views.lostform, name='lostform'),
    path('lostfound/found', views.found, name='found'),
    path('lostfound/found/foundform', views.foundform, name='foundform'),
    path('cabsharing', views.cabsharing, name='cabsharing'),
    path('cabsharing/cabsharingform', views.cabsharingform, name='cabsharingform'),
]
