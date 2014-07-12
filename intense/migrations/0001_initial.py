# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePage'
        db.create_table(u'intense_homepage', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subheading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('featured_portfolio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['intense.Portfolio'], null=True, blank=True)),
            ('featured_portfolio_header', self.gf('django.db.models.fields.CharField')(default='Featured work', max_length=100)),
            ('featured_portfolio_lead', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('our_clients_header', self.gf('django.db.models.fields.CharField')(default='Our clients', max_length=100)),
            ('our_clients_lead', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'intense', ['HomePage'])

        # Adding model 'Slide'
        db.create_table(u'intense_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['intense.HomePage'])),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'intense', ['Slide'])

        # Adding model 'IconBox'
        db.create_table(u'intense_iconbox', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='boxes', to=orm['intense.HomePage'])),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'intense', ['IconBox'])

        # Adding model 'Client'
        db.create_table(u'intense_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clients', to=orm['intense.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'intense', ['Client'])

        # Adding model 'Portfolio'
        db.create_table(u'intense_portfolio', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('columns', self.gf('django.db.models.fields.CharField')(default='3', max_length=1)),
        ))
        db.send_create_signal(u'intense', ['Portfolio'])

        # Adding model 'PortfolioItem'
        db.create_table(u'intense_portfolioitem', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('subheading', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('featured_image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('client_description', self.gf('mezzanine.core.fields.RichTextField')(blank=True)),
            ('href', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
        ))
        db.send_create_signal(u'intense', ['PortfolioItem'])

        # Adding M2M table for field categories on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'intense_portfolioitem_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('portfolioitem', models.ForeignKey(orm[u'intense.portfolioitem'], null=False)),
            ('portfolioitemcategory', models.ForeignKey(orm[u'intense.portfolioitemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['portfolioitem_id', 'portfolioitemcategory_id'])

        # Adding M2M table for field related_items on 'PortfolioItem'
        m2m_table_name = db.shorten_name(u'intense_portfolioitem_related_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_portfolioitem', models.ForeignKey(orm[u'intense.portfolioitem'], null=False)),
            ('to_portfolioitem', models.ForeignKey(orm[u'intense.portfolioitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_portfolioitem_id', 'to_portfolioitem_id'])

        # Adding model 'PortfolioItemImage'
        db.create_table(u'intense_portfolioitemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('portfolioitem', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['intense.PortfolioItem'])),
            ('file', self.gf('mezzanine.core.fields.FileField')(max_length=200)),
        ))
        db.send_create_signal(u'intense', ['PortfolioItemImage'])

        # Adding model 'PortfolioItemCategory'
        db.create_table(u'intense_portfolioitemcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal(u'intense', ['PortfolioItemCategory'])


    def backwards(self, orm):
        # Deleting model 'HomePage'
        db.delete_table(u'intense_homepage')

        # Deleting model 'Slide'
        db.delete_table(u'intense_slide')

        # Deleting model 'IconBox'
        db.delete_table(u'intense_iconbox')

        # Deleting model 'Client'
        db.delete_table(u'intense_client')

        # Deleting model 'Portfolio'
        db.delete_table(u'intense_portfolio')

        # Deleting model 'PortfolioItem'
        db.delete_table(u'intense_portfolioitem')

        # Removing M2M table for field categories on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'intense_portfolioitem_categories'))

        # Removing M2M table for field related_items on 'PortfolioItem'
        db.delete_table(db.shorten_name(u'intense_portfolioitem_related_items'))

        # Deleting model 'PortfolioItemImage'
        db.delete_table(u'intense_portfolioitemimage')

        # Deleting model 'PortfolioItemCategory'
        db.delete_table(u'intense_portfolioitemcategory')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'generic.assignedkeyword': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'AssignedKeyword'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': u"orm['generic.Keyword']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {})
        },
        u'generic.keyword': {
            'Meta': {'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'intense.client': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Client'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clients'", 'to': u"orm['intense.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'intense.homepage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'featured_portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['intense.Portfolio']", 'null': 'True', 'blank': 'True'}),
            'featured_portfolio_header': ('django.db.models.fields.CharField', [], {'default': "'Featured work'", 'max_length': '100'}),
            'featured_portfolio_lead': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'our_clients_header': ('django.db.models.fields.CharField', [], {'default': "'Our clients'", 'max_length': '100'}),
            'our_clients_lead': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'intense.iconbox': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'IconBox'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'boxes'", 'to': u"orm['intense.HomePage']"}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'intense.portfolio': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Portfolio', '_ormbases': [u'pages.Page']},
            'columns': ('django.db.models.fields.CharField', [], {'default': "'3'", 'max_length': '1'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'intense.portfolioitem': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'PortfolioItem', '_ormbases': [u'pages.Page']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'portfolioitems'", 'blank': 'True', 'to': u"orm['intense.PortfolioItemCategory']"}),
            'client_description': ('mezzanine.core.fields.RichTextField', [], {'blank': 'True'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'featured_image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'href': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'related_items': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_items_rel_+'", 'blank': 'True', 'to': u"orm['intense.PortfolioItem']"}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'intense.portfolioitemcategory': {
            'Meta': {'ordering': "('title',)", 'object_name': 'PortfolioItemCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'intense.portfolioitemimage': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'PortfolioItemImage'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'file': ('mezzanine.core.fields.FileField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolioitem': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['intense.PortfolioItem']"})
        },
        u'intense.slide': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Slide'},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['intense.HomePage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'pages.page': {
            'Meta': {'ordering': "('titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords': ('mezzanine.generic.fields.KeywordsField', [], {'object_id_field': "'object_pk'", 'to': u"orm['generic.AssignedKeyword']", 'frozen_by_south': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['intense']