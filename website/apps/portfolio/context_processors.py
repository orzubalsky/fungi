from django.conf import settings
from portfolio.models import *

def projects(request):

    projects = Project.objects.filter(is_active=True)
    navigation_tagbag = TagBag.objects.filter(is_active=True)[0]

    return { 'projects' : projects, 'navigation_tagbag' : navigation_tagbag }

def google_analytics(request):
    if settings.GOOGLE_ANALYTICS_KEY:
        return { 'GOOGLE_ANALYTICS_KEY' : settings.GOOGLE_ANALYTICS_KEY }
