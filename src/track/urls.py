#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns

from music_website.urls import ROUTER
from track.views import TrackViewSet

app_name = 'track'

ROUTER.register('tracks', TrackViewSet, base_name='track')

urlpatterns = [
    # path('api/<int:pk>/', TrackDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
