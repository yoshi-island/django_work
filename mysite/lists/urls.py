from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='lists'),
    url(r'^info/', views.info , name='info'),
    url(r'^create/', views.create , name='create'),
    url(r'^update/1/', views.test, name='update'),
    url(r'^update/$', views.info, name='update_index'),
]

