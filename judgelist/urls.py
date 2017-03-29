from django.conf.urls import url,include
from . import views
#try


urlpatterns = [
    url(r'^$', views.judge_list, name='judge_list'),
]
