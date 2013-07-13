from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from portfolio.views import *

# 
# @dajaxice_register(method='POST')
# def ajax_load(request, slug=None):
#     """ """
#     return ProjectList(request)