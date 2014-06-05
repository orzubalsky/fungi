from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from portfolio.views import *

# orzubalskydotcom application
urlpatterns = patterns('portfolio.views',
    url(r'bio$', TemplateView.as_view(template_name="bio.html"), name='bio'),
    url(r'statement$', TemplateView.as_view(template_name="statement.html"), name='statement'),    
    url(r'project/(?P<slug>[0-9A-Za-z\-]+)$', ProjectDetail.as_view(), name='project-detail'),
    url(r'experiment/(?P<slug>[0-9A-Za-z\-]+)$', ExperimentDetail.as_view(), name='experiment-detail'),
    url(r'$', ProjectList.as_view(template_name="project_list.html"), name='project-list'),
)