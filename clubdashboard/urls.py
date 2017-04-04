from django.conf.urls import url,include
from . import views


app_name= 'clubdashboard'

urlpatterns = [
    url(r'^$', views.clubdashboard, name='clubdashboard'),
]