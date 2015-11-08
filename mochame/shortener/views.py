# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.views.generic import View
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404

from shortener.baseconv import base62

from .models import Link
from .serializers import LinkSerializer


class FollowView(View):
    """
        View which gets the link for the given base62_id value
        and redirects to it.
    """
    def get(self, request, base62_id):
        link = get_object_or_404(Link, id=base62.to_decimal(base62_id))
        link.clicks = link.clicks + 1
        link.save()
        return HttpResponsePermanentRedirect(link.target_url)

# Api response
class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    permission_classes = (AllowAny,)
    queryset = Link.objects.all()
    filter_fields = ('target_url', 'short_url',)

