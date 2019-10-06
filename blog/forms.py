from django import forms

from .models import Post, Information

class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]

class InformationForm(forms.ModelForm):
    # content = forms.TextField(required = True)

    class Meta:
        model = Information
        fields = ('name','subject','email','message')