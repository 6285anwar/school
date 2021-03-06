"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from teacher import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),

    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),
    re_path(r'^addteacher/$', views.addteacher, name='addteacher'),
    re_path(r'^typeinput/$', views.typeinput, name='typeinput'),
    re_path(r'^profile/(?P<id>\d+)/$', views.profile, name='profile'),
    re_path(r'^upload_csv/$', views.upload_csv, name='upload_csv'),





]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
