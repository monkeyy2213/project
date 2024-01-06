from django.urls import path

from .views import *


urlpatterns = [
    path('', AnimalHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_animals/', AddAnimals.as_view(), name='add_animals'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('service/', Service.as_view(), name='service'),
]