from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from taggit.models import Tag
from portfolio.models import *
from portfolio.forms import *


class PostList(ListView):
    """
    """
    queryset = Post.objects.filter(is_active=True)
    template_name = 'post_list.html'


class PostDetail(DetailView):
    """
    """
    model = Post
    template_name = 'post_detail.html'


class ProjectDetail(DetailView):
    """
    """
    model = Project
    template_name = 'project_detail.html'


class ExperimentDetail(DetailView):
    """
    """
    model = Experiment
    template_name = 'experiment_detail.html'


def project_list(request):
    """
    """
    projects = Project.objects.filter(is_active=True)
    experiments = Experiment.objects.filter(is_active=True)

    return render_to_response('project_list.html', {
        'projects': projects,
        'experiments': experiments,
    }, context_instance=RequestContext(request))


def tagged_projects(request, slug=None):
    """
    """
    tag = get_object_or_404(Tag, slug=slug)
    
    projects = Project.objects.filter(tags__name__in=[tag.name,])
    
    return render_to_response('tagged_projects.html', {
            'tagged_projects' : projects,
            'tag'             : tag
        }, context_instance = RequestContext(request))