from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='apps'),
    url(r'^meeting-timer/', TemplateView.as_view(template_name='meeting-timer.html') , name='meeting-timer'),
    url(r'^twitter-place/', TemplateView.as_view(template_name='twitter-place.html') , name='twitter-place'),
    url(r'^epoch-graph/', TemplateView.as_view(template_name='epoch-graph.html') , name='epoch-graph'),
]

