from django.urls import path

from .views import Login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
