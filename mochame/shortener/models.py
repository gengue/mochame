# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sites.models import Site

from config.settings.local import CURRENT_DOMAIN
from .baseconv import base62


class Link(models.Model):
    short_url = models.URLField(unique=True, null=True, blank=True)
    target_url = models.URLField()
    clicks = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.skip_signal = True
        super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.target_url

# signal post-save function
@receiver(post_save, sender=Link)
def shortener_url(sender, instance, **kwargs):
    if not instance.short_url:
        uuid = base62.from_decimal(instance.id)
        instance.short_url = "%s%s" % (CURRENT_DOMAIN, uuid)
        instance.save()
