from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('users.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^profile_page/', include('profile_page.urls')),
    url(r'^student_list/', include('studentlist.urls')),
    url(r'^judge_list/', include('judgelist.urls')),
    url(r'^clubdashboard/', include('clubdashboard.urls')),
    url(r'^studentdashboard/', include('studentdashboard.urls')),
    url(r'^judgedashboard/', include('judgedashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
