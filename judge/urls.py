from django.conf.urls import url,include
from . import views


app_name= 'judge'

urlpatterns = [
    url(r'^$', views.judge_page, name='judge_details'),
]