from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


#delete later

def judge_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if not request.user.judge:
        return HttpResponseRedirect('/user/student_details')
    user = request.user
    context = {'user':user,}
    return render(request,'judge/judge_page.html',context)
