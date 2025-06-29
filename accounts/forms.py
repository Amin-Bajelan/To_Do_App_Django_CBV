from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_pic', 'bio']
