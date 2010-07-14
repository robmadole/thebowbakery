# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Bow'
        db.create_table('inventory_bow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('available', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('inventory', ['Bow'])


    def backwards(self, orm):
        
        # Deleting model 'Bow'
        db.delete_table('inventory_bow')


    models = {
        'inventory.bow': {
            'Meta': {'object_name': 'Bow'},
            'available': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['inventory']
