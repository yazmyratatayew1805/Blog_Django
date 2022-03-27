from django import forms
from .models import Post, Comment






class CommentForm(forms.ModelForm):
    Teswir = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Teswiriňi ýaz!','id': 'usercomment','rows': '4'}))
    class Meta:
        model = Comment
        fields = ('Teswir',)


# class Login_Form(forms.Form):
#     username=forms.CharField(widget=forms.TextInput(attrs={'class':'col-md-10'}))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'col-md-10'}))


# class Register_Form(forms.Form):
#     username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-group col-md-10'}))
#     first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-group col-md-10'}))
#     last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-group col-md-10'}))
#     parol=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group col-md-10'}))