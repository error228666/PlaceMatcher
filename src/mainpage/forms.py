from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ImageField
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs=
                                                                {'placeholder': 'Имя', 'class': 'form-control', }))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                              'class': 'form-control', }))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя',
                                                             'class': 'form-control',}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control', }))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                  'class': 'form-control', 'data-toggle': 'password',
                                                                  'id': 'password', }))
    password2 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердить пароль', 'class': 'form-control',
                                                                  'data-toggle': 'password', 'id': 'password', }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя', 'class': 'form-control',}))
    password = forms.CharField(max_length=50, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form-control',
                                                                 'data-toggle': 'password', 'id': 'password',
                                                                 'name': 'password', }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):
    avatar: ImageField = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


"""
class MeetingForm(forms.ModelForm):
    friends =

    class Meta:
        model = Meeting
        fields = ['', 'bio']
"""