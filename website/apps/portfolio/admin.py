from django.conf import settings
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.forms.widgets import Textarea
from django.contrib import admin
from filebrowser.widgets import FileInput
from portfolio.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    """
    pass


class OrderedTagInline(admin.TabularInline):
    """
    """
    model           = OrderedTag
    fields          = ('tag', 'position')
    extra           = 0
    sortable_field_name = 'position'
    


class ProjectAdmin(BaseAdmin):
    """
    """
    class Media:
        widgets = {
                'credits': Textarea,
                }              
            
    fieldsets = (
        ('Info', {
            'fields': ('name', 'slug', 'groups', 'content', 'medium', 'project_time', 'material', 'dimensions', 'project_link', 'source_link', 'credits', 'position', 'is_active')
        }),
        ('Meta', {
            'fields': ('gallery_style', 'tags', 'related_projects')
        }),        
        ('Media', {
            'fields': ('images', 'sounds', 'videos', 'vimeos', 'documents')
        }),     
    )
    list_display        = ('name', 'position', 'is_active') 
    list_editable       = ('position', 'is_active',)
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(BaseAdmin):
    """
    """
    fieldsets    = (
        ('Info', {
            'fields': ('name', 'content', 'slug', 'source_link', 'projects', 'is_active')
        }),
        ('Media', {
            'fields': ('images', 'sounds', 'videos', 'vimeos', 'documents')
        }),
    )
    list_display        = ('name', 'is_active') 
    list_editable       = ('is_active',)    
    prepopulated_fields = {'slug': ('name',)}
             

class OrderedTagAdmin(BaseAdmin):
    """
    """
    list_display        = ('tag', 'position') 
    list_editable       = ('position',)    


class TagBagAdmin(BaseAdmin):
    """
    """
    list_display        = ('name', 'is_active') 
    list_editable       = ('is_active',)    
    inlines             = (OrderedTagInline,)
    


# register admin models
admin.site.register(Image)
admin.site.register(Sound)
admin.site.register(Document)
admin.site.register(Video)
admin.site.register(Vimeo)
admin.site.register(Group)
admin.site.register(OrderedTag, OrderedTagAdmin)
admin.site.register(TagBag, TagBagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)