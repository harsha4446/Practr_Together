from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def profile_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    if request.user.judge:
        return HttpResponseRedirect('/user/judge_details')
    current_user = request.user
    context = {"user":current_user,}
    return render(request,'profile_page/profile_page.html',context)