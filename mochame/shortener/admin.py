# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Link



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    exclude = ('short_url', 'clicks',)
    list_display = ('target_url', 'short_url', 'clicks', 'pub_date',)
    ordering = ('-pub_date',)

