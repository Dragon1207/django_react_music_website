#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from music.models import Album, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title',)


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'songs',)

    songs = SongSerializer(many=True)
