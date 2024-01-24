from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):
    gender_choices = (
        ('M', 'Male'),
        ("F", 'Female')
    )

    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    birthday = models.DateField(auto_now_add=True)
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect())
