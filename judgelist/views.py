from django.shortcuts import render

from judgelist.forms import userForm, nameForm, designationForm
from users.models import student

# Create your views here.
def judge_list(request):
    all_users = student.objects.filter(judge=True)
    formuser = userForm(request.POST or None)
    formdesignation = designationForm(request.POST or None)
    formname = nameForm(request.POST or None)

    if formuser.is_valid() and formuser.cleaned_data['email'] != '':
        email = formuser.cleaned_data['email']
        all_users = student.objects.filter(judge=True, email=email)

    if formname.is_valid() and formname.cleaned_data['name'] != '':
        name = formname.cleaned_data['name']
        all_users = student.objects.filter(judge=True, name=name)

    if formdesignation.is_valid() and formdesignation.cleaned_data['designation'] != '':
        designation = formdesignation.cleaned_data['designation']
        all_users = student.objects.filter(judge=True, designaiton=designation)
    context = {"all_users":all_users,}
    return render (request,'judge_list/judge_list.html',context)
