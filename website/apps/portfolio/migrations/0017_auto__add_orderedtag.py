# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrderedTag'
        db.create_table(u'portfolio_orderedtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tagbag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.TagBag'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taggit.Tag'])),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'portfolio', ['OrderedTag'])

        # Removing M2M table for field tags on 'TagBag'
        db.delete_table(db.shorten_name(u'portfolio_tagbag_tags'))


    def backwards(self, orm):
        # Deleting model 'OrderedTag'
        db.delete_table(u'portfolio_orderedtag')

        # Adding M2M table for field tags on 'TagBag'
        m2m_table_name = db.shorten_name(u'portfolio_tagbag_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tagbag', models.ForeignKey(orm[u'portfolio.tagbag'], null=False)),
            ('tag', models.ForeignKey(orm[u'taggit.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tagbag_id', 'tag_id'])


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portfolio.document': {
            'Meta': {'object_name': 'Document'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'media': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'media': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.orderedtag': {
            'Meta': {'object_name': 'OrderedTag'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['taggit.Tag']"}),
            'tagbag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.TagBag']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Document']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Image']", 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Project']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '160'}),
            'sounds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Sound']", 'null': 'True', 'blank': 'True'}),
            'source_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Video']", 'null': 'True', 'blank': 'True'}),
            'vimeos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Vimeo']", 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.project': {
            'Meta': {'ordering': "['position']", 'object_name': 'Project'},
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'credits': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Document']", 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Image']", 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'material': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'project_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'project_time': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'related_projects': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_projects_rel_+'", 'null': 'True', 'to': u"orm['portfolio.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '160'}),
            'sounds': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Sound']", 'null': 'True', 'blank': 'True'}),
            'source_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {}),
            'videos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Video']", 'null': 'True', 'blank': 'True'}),
            'vimeos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['portfolio.Vimeo']", 'null': 'True', 'blank': 'True'})
        },
        u'portfolio.sound': {
            'Meta': {'object_name': 'Sound'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'media': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.tagbag': {
            'Meta': {'object_name': 'TagBag'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['taggit.Tag']", 'symmetrical': 'False', 'through': u"orm['portfolio.OrderedTag']", 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.video': {
            'Meta': {'object_name': 'Video'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'media': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'portfolio.vimeo': {
            'Meta': {'object_name': 'Vimeo'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'media': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['portfolio']