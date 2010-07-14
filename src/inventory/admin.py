from django.contrib import admin

from inventory.models import Bow

class BowAdmin(admin.ModelAdmin):
    list_display = ('product_number', 'admin_image', 'price', 'available',)

admin.site.register(Bow, BowAdmin)
