from django import forms
from .models import Signup,Notes

class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'
        #fields=['id','name','email','password','mobile']

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields='__all__'
        