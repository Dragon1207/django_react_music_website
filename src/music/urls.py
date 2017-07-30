#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.AlbumListView.as_view(), name='album_list'),
    url(r'^(?P<pk>\d+)$', views.AlbumDetailView.as_view(), name='album_detail'),
]
