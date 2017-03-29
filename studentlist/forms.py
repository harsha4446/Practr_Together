from django import forms

class userForm(forms.Form):
    email = forms.CharField(label="",required=False)


class nameForm(forms.Form):
    name = forms.CharField(label="",required=False)

class collegeForm(forms.Form):
    college = forms.CharField(label="",required=False)