from django.shortcuts import render
from users.models import student
from . forms import userForm,collegeForm,nameForm


# Create your views here.

def student_list(request):
    colleg_field = ''
    all_users = student.objects.filter(judge=False)
    formuser = userForm(request.POST or None)
    formcollege = collegeForm(request.POST or None)
    formname = nameForm(request.POST or None)

    if formuser.is_valid() and formuser.cleaned_data['email'] != '':
        email = formuser.cleaned_data['email']
        all_users = student.objects.filter(judge=False,email=email)

    if formname.is_valid()and formname.cleaned_data['name'] != '':
        name = formname.cleaned_data['name']
        all_users = student.objects.filter(judge=False,name=r'^[name]$')

    if formcollege.is_valid()and formcollege.cleaned_data['college'] != '':
        college = formcollege.cleaned_data['college']
        all_users = student.objects.filter(judge=False,college=college)
    print(colleg_field)
    print("something")
    context = {"all_users":all_users,"email":formuser,"name":formname,"college":formcollege,"college_field":colleg_field,}
    return render (request,'student_list/student_list.html',context)