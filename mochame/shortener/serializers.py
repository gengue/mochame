# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import Link



class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('id', 'target_url', 'short_url', 'clicks', 'pub_date',)
        read_only_fields = ('id', 'short_url', 'clicks',)



