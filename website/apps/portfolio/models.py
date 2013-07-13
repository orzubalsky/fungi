from django.conf import settings
from django.db.models import *
from django.utils import timezone
from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from taggit.managers import TaggableManager
from taggit.models import Tag
import pytz, os



class Base(Model):
    """ Base model for all of the models in the application.
    """
    class Meta:
        abstract = True
    
    # Translators:  Used wherever a created time stamp is needed.                   
    created     = DateTimeField(editable=False)
    
    # Translators: Used wherever an update time stamp is needed.
    updated     = DateTimeField(editable=False)
    
    # Translators: Used to determine whether something is active in the front end or not.
    is_active   = BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        """ Save timezone-aware values for created and updated fields.
        """
        if self.pk is None:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Base, self).save(*args, **kwargs)
        
    def __unicode__ (self):
        if hasattr(self, "name") and self.name:
            return self.name
        else:
            return "%s" % (type(self))


class Image(Base):
    name  = CharField(max_length=140, null=True, blank=True)
    media = FileBrowseField("Image", max_length=200, directory="images/")
    

class Document(Base):
    name  = CharField(max_length=140, null=True, blank=True)    
    media = FileBrowseField("PDF", max_length=200, directory="documents/")


class Sound(Base):
    name  = CharField(max_length=140, null=True, blank=True)    
    media = FileBrowseField("Audio", max_length=200, directory="sounds/")


class Video(Base):
    name  = CharField(max_length=140, null=True, blank=True)    
    media = FileBrowseField("Video", max_length=200, directory="video/")


class Vimeo(Base):
    name     = CharField(max_length=140, null=True, blank=True)
    media    = TextField()


class ContentManager(Manager):
    def get_query_set(self):
        return super(ContentManager, self).get_query_set().prefetch_related('images', 'sounds', 'videos', 'vimeos', 'documents')

class Content(Base):
    """
    """
    class Meta:
        abstract = True
      
    name         = CharField(max_length=140)
    content      = HTMLField(null=True, blank=True)
    slug         = SlugField(max_length=160)
    images       = ManyToManyField(Image, blank=True, null=True)
    sounds       = ManyToManyField(Sound, blank=True, null=True)
    videos       = ManyToManyField(Video, blank=True, null=True)
    vimeos       = ManyToManyField(Vimeo, blank=True, null=True)
    documents    = ManyToManyField(Document, blank=True, null=True)
    source_link  = URLField(blank=True, null=True)

    objects = ContentManager()

    def media():
        def fget(self):
            return {'images'    : self.images, 
                    'sounds'    : self.sounds, 
                    'videos'    : self.videos,
                    'vimeos'    : self.vimeos, 
                    'documents' : self.documents, 
                    }
        return locals()

    media = property(**media())
    
    def gallery_items(self):
        items = []
        for item_dictionary in self.media.values():
            if item_dictionary.count() > 0:
                for item in item_dictionary.all():
                    items.append(item)
        return items

    def gallery_items_count(self):
        return len(self.gallery_items())
        
class Group(Base):
    """
    """
    name  = CharField(max_length=140, null=False, blank=False)


class Project(Content):
    """
    """
    class Meta:
        ordering = ['position',]

    position         = PositiveSmallIntegerField(default=0)
    project_time     = CharField(max_length=140, blank=True, null=True) 
    medium           = CharField(max_length=255, blank=True, null=True)
    material         = CharField(max_length=255, blank=True, null=True)
    dimensions       = CharField(max_length=255, blank=True, null=True)
    credits          = TextField(blank=True, null=True)
    project_link     = URLField(blank=True, null=True)
    groups           = ManyToManyField(Group, blank=True, null=True)
    tags             = TaggableManager(blank=True)
    related_projects = ManyToManyField('self', blank=True, null=True)
    
    def tag_class_list(self):
        return " ".join(["%s" % (t.name) for t in self.tags.all()])


class Post(Content):
    """
    """
    class Meta:
        ordering = ['-created',]
    
    projects    = ManyToManyField(Project, blank=True, null=True)


class TagBag(Base):
    name = CharField(max_length=140, null=False, blank=False)
    tags = ManyToManyField(Tag, through='OrderedTag', blank=True)
    
    
class OrderedTag(Base):
    tagbag    = ForeignKey(TagBag)
    tag       = ForeignKey(Tag)
    position  = PositiveSmallIntegerField(default=0)


# signals are separated to signals.py 
# just for the sake of organization
import signals