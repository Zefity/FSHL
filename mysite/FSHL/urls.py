from django.urls import path, include

from FSHL.views import products

app_name = 'FSHL'

urlpatterns = [
    path('', products, name='index')
]
