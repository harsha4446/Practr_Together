from django import forms
from . models import student
from django.contrib.auth import (authenticate,login,logout,get_user_model)
from django.forms.extras import SelectDateWidget

user = get_user_model()

class RegisterModel(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = student
        fields = ['email','password','name','phoneno',]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


DOY = ('1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987',
       '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003',
       '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011',
       '2012', '2013', '2014', '2015', '2016', '2017', '2018',)



class StudentInfo(forms.ModelForm):
    dob = forms.DateField(widget=SelectDateWidget(years = DOY))
    location = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    college = forms.CharField(label="",required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    profile_picture = forms.ImageField(label="",required=False,widget=forms.TextInput(attrs={'class' : 'picture-src'}))
    class Meta:
        model = student
        fields = ['profile_picture','location','degree', 'college', 'year','dob',]


class JudgeInfo(forms.ModelForm):
    dob = forms.DateField(widget=SelectDateWidget(years = DOY))
    class Meta:
        model = student
        fields = ['profile_picture','location','degree', 'designation','dob', 'industry_exp','website',]