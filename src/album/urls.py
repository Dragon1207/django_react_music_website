#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from album.views import AlbumCreate, AlbumDelete, AlbumDetail, AlbumList, AlbumUpdate, AlbumViewSet
from music_website.urls import ROUTER

app_name = 'album'

ROUTER.register('albums', AlbumViewSet, base_name='album')

urlpatterns = [
    path('', AlbumList.as_view(), name='list'),
    path('create/', AlbumCreate.as_view(), name='create'),
    path('<slug:slug>/', AlbumDetail.as_view(), name='detail'),
    path('<slug:slug>/update/', AlbumUpdate.as_view(), name='update'),
    path('<slug:slug>/delete/', AlbumDelete.as_view(), name='delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
