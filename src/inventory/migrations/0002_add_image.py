# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Bow.image'
        db.add_column('inventory_bow', 'image', self.gf('django.db.models.fields.files.ImageField')(default='empty.png', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Bow.image'
        db.delete_column('inventory_bow', 'image')


    models = {
        'inventory.bow': {
            'Meta': {'object_name': 'Bow'},
            'available': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'empty.png'", 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['inventory']
