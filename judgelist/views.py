from django.shortcuts import render
from users.models import student
from studentlist.forms import userForm,collegeForm,nameForm

# Create your views here.
def judge_list(request):
     all_users = student.objects.filter(judge=True)
     formuser = userForm(request.POST or None)
     formcollege = collegeForm(request.POST or None)
     formname = nameForm(request.POST or None)

     if formuser.is_valid() and formuser.cleaned_data['email'] != '':
        email = formuser.cleaned_data['email']
        all_users = student.objects.filter(judge=True, email=email)

     if formname.is_valid() and formname.cleaned_data['name'] != '':
        name = formname.cleaned_data['name']
        all_users = student.objects.filter(judge=True, name=name)

     if formcollege.is_valid() and formcollege.cleaned_data['college'] != '':
        college = formcollege.cleaned_data['college']
        all_users = student.objects.filter(judge=True, college=college)

     context = {"all_users": all_users, "email": formuser, "name": formname, "college": formcollege, }
     return render(request, 'judge_list/judge_list.html', context)
