from django.conf.urls import url
from . import views

app_name = 'vacation'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^summary/$', views.summary, name='summary'),
    url(r'^csv/$', views.dump_csv, name='dump_csv'),
    url(r'^detail/(?P<name>[\w]+)/$', views.detail, name='detail')
]
