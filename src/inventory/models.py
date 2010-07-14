from django.db import models
from django.conf import settings


class Bow(models.Model):
    image = models.ImageField(upload_to='bow', null=False, blank=False,
        default='bow/empty.png')
    price = models.DecimalField(null=False, blank=False, max_digits=5,
        decimal_places=2)
    available = models.IntegerField(null=False, blank=False, default=1,
        help_text='How many are there to sell?')
    date_added = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    date_changed = models.DateTimeField(
        auto_now=True, auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'Bow %s' % self.pk

    def product_number(self):
        return u'%s%s' % (settings.PRODUCT_NUMBER_PREFIX.upper(),
            self.pk)

    def admin_image(self):
        return u'<img src="%s" width="128" />' % self.image.url
    admin_image.short_description = 'Image'
    admin_image.allow_tags = True
