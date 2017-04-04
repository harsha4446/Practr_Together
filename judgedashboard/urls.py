from django.conf.urls import url,include
from . import views


app_name= 'judgedashboard'

urlpatterns = [
    url(r'^$', views.judgedashboard, name='judgedashboard'),
]