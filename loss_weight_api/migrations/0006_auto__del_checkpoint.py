# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CheckPoint'
        db.delete_table('loss_weight_api_checkpoint')


    def backwards(self, orm):
        # Adding model 'CheckPoint'
        db.create_table('loss_weight_api_checkpoint', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('isPlanned', self.gf('django.db.models.fields.BooleanField')()),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loss_weight_api.User'])),
        ))
        db.send_create_signal('loss_weight_api', ['CheckPoint'])


    models = {
        'loss_weight_api.user': {
            'Meta': {'object_name': 'User'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'current_waight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_waight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'registration_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'})
        }
    }

    complete_apps = ['loss_weight_api']