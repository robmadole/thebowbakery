# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Bow.date_added'
        db.add_column('inventory_bow', 'date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True), keep_default=False)

        # Adding field 'Bow.date_changed'
        db.add_column('inventory_bow', 'date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Bow.date_added'
        db.delete_column('inventory_bow', 'date_added')

        # Deleting field 'Bow.date_changed'
        db.delete_column('inventory_bow', 'date_changed')


    models = {
        'inventory.bow': {
            'Meta': {'object_name': 'Bow'},
            'available': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'empty.png'", 'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['inventory']
