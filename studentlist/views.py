from django.shortcuts import render
from users.models import student
# Create your views here.

def student_list(request):
    all_users = student.objects.filter(judge=False)
    context = {"all_users":all_users,}
    return render (request,'student_list/student_list.html',context)