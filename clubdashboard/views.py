
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def clubdashboard(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/home/')
    user = request.user
    context = {'user':user,}
    return render(request, 'club/dashboard/dashboard.html', context)
