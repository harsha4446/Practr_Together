from django.conf.urls import url,include
from . import views


#yrls

urlpatterns = [
    url(r'^$', views.profile_page, name='profile_page'),
]
