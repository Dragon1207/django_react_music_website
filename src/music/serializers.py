#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from music.models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'title',)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'tracks',)

    tracks = TrackSerializer(many=True)
