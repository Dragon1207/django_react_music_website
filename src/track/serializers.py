#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from track.models import Track


class TrackSerializer(serializers.ModelSerializer):
    """
    This serializer used for TrackViewSet
    """

    class Meta:
        model = Track
        fields = ('id', 'album', 'title')


class TrackUpdateSerializer(serializers.ModelSerializer):
    """
    This serializer used for AlbumSerializer to be able to create new Tracks during Album partial update
    """

    # To be possible to make Album partial update with creating new tracks Track.id field should be not read_only
    # It is read_only by default as a PK
    id = serializers.IntegerField(label='ID')

    class Meta:
        model = Track
        # According to 'album' field, I suppose that during updating Album it will be not possible to change album
        # for track
        fields = ('id', 'title')
