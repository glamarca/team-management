from django.conf.urls import url
from django.contrib.auth.views import login, logout

app_name = "vacation"

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # login / logout urls
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
]
