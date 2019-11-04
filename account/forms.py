from django.contrib.auth.models import User
from django import forms

from .models import Profile,Type

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='',
         widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}
        ))
    password2 = forms.CharField(label='',
         widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}
        ))
    username = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        ))
    email = forms.EmailField(label='',
       widget=forms.EmailInput(
           attrs={'class': 'form-control', 'placeholder': 'Email'}
       ))

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
            attrs={'class': 'form-control', 'placeholder': 'Enter First Name','label':''}
        ),label='',
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Last Name',}
        ),label='',
    )
    agent_type = forms.ModelChoiceField(
        queryset=Type.objects.all(), to_field_name='id', required=True,
        widget=forms.Select(
            attrs={'class': 'form-control', 'placeholder': 'agent type',}
        ),label='',)

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'eg: +234 8030793112','label':''}
        ),label='',
    )

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','phone','agent_type')



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
    agent_type = forms.ModelChoiceField(
        queryset=Type.objects.all(), to_field_name='id', required=True)

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Address'}
        ), required=False
    )
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})
                                  ,label='About', required=False)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name','phone', 'address', 'photo','agent_type',
                  'facebook','twitter','google','linkedin','description')

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'class': 'filestyle'})