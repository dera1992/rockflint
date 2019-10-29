from django import forms

class MessageForm(forms.Form):
    phone = forms.CharField(max_length=25,required=False,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Phone', }
                           ), label='',
                           )
    email = forms.EmailField(
        label='',required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'}
        )
    )
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(
                               attrs={'class': 'form-control', 'placeholder': 'Message', }
                           ), label='',)


class ScheduleForm(forms.Form):
    date = forms.DateField(required=False,
                           widget=forms.DateInput(
                               attrs={'class': 'form-control', 'placeholder': 'Date', }
                           ), label='',
                           )
    time = forms.TimeField( required=False,
                            widget=forms.TimeInput(
                                attrs={'class': 'form-control', 'placeholder': 'Time', }
                            ), label='',
                            )
    name = forms.CharField(max_length=255, required=False,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Name', }
                            ), label='',
                            )
    phone = forms.CharField(max_length=25, required=False,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Phone', }
                            ), label='',
                            )

    message = forms.CharField(required=False,
                               widget=forms.Textarea(
                               attrs={'class': 'form-control', 'placeholder': 'Message', }
                           ), label='',)

