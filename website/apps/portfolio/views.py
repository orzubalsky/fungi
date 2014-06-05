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


class ProjectList(ListView):
    """
    """
    def get_context_data(self, **kwargs):
            # Call the base implementation first to get a context
            context = super(ProjectList, self).get_context_data(**kwargs)
            context['experiments'] = Experiment.objects.all()

            return context

    queryset = Project.objects.filter(is_active=True)
    print queryset
    template_name = 'project_list.html'


def tagged_projects(request, slug=None):
    """
    """
    tag = get_object_or_404(Tag, slug=slug)
    
    projects = Project.objects.filter(tags__name__in=[tag.name,])
    
    return render_to_response('tagged_projects.html', {
            'tagged_projects' : projects,
            'tag'             : tag
        }, context_instance = RequestContext(request))