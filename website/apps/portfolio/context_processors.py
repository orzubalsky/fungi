from portfolio.models import *

def projects(request):
    projects = Project.objects.filter(is_active=True)
    project = projects[0]
    return { 'projects' : projects, 'project' : project }
