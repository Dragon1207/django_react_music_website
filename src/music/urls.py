#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?:page/(?P<page>\d+))?$', views.AlbumListView.as_view(), name='album_list'),
    url(r'^(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^album/create/$', views.AlbumCreateView.as_view(), name='album_create'),
    url(r'^album/(?P<pk>\d+)/$', views.AlbumUpdateView.as_view(), name='album_update'),
    url(r'^album/(?P<pk>\d+)/delete/$', views.AlbumDeleteView.as_view(), name='album_delete'),
]
