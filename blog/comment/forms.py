from django import forms
from .models import Comments


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '7','cols':'90','class':'form-control',
                   'placeholder': 'Say Something...'},
        ))

    class Meta:
        model = Comments
        fields = ['body']



class PostFormChild(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': '1','cols':'90','class':'form-control',
                   'placeholder': 'Say Something...'},
        ))

    class Meta:
        model = Comments
        fields = ['body']