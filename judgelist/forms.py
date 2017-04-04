from django import forms

class userForm(forms.Form):
    email = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))


class nameForm(forms.Form):
    name = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder': 'Name'}))

class designationForm(forms.Form):
    designation = forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder': 'designation'}))