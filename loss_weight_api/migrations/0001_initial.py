# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('loss_weight_api_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('current_waight', self.gf('django.db.models.fields.IntegerField')()),
            ('initial_waight', self.gf('django.db.models.fields.IntegerField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('registration_date', self.gf('django.db.models.fields.DateField')(blank=True, auto_now_add=True)),
        ))
        db.send_create_signal('loss_weight_api', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('loss_weight_api_user')


    models = {
        'loss_weight_api.user': {
            'Meta': {'object_name': 'User'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'current_waight': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_waight': ('django.db.models.fields.IntegerField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'})
        }
    }

    complete_apps = ['loss_weight_api']