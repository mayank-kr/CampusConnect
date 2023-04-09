from django.urls import path
# from .views import GoogleLoginView
from . import views

urlpatterns = [
    path('importantContacts/emergency', views.emergency, name='emergency'),
    path('importantContacts/administration',
         views.administration, name='administration'),
    path('importantContacts/faculty', views.faculty, name='faculty'),
    path('profile', views.profile, name='profile'),
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),
    path('lostfound/lost', views.lost, name='lost'),
    # path('accounts/google/login/', GoogleLoginView.as_view(), name='google_login'),
]
