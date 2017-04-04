from django.conf.urls import url,include
from . import views


app_name= 'studentdashboard'

urlpatterns = [
    url(r'^$', views.studentdashboard, name='studentdashboard'),
]