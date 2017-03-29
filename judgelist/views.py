from django.shortcuts import render
from users.models import student

# Create your views here.
def judge_list(request):
    all_users = student.objects.filter(judge=True)
    context = {"all_users":all_users,}
    return render (request,'judge_list/judge_list.html',context)
