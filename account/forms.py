from django.contrib.auth.models import User
from django import forms

from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'eg: +234 8030793112'}
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
        )
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','phone', 'address', 'photo')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'filestyle'})


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'eg: +234 8030793112'}
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
        )
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','phone', 'address', 'photo')
