
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class FarmerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'phone', 'address', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'farmer'
        user.status = 'pending'
        if commit:
            user.save()
        return user


class OfficerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'phone', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'officer'
        user.status = 'active'
        if commit:
            user.save()
        return user
