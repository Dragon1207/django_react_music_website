#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from music.models import Album, Track


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


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'tracks')

    tracks = TrackUpdateSerializer(many=True)

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    def update(self, instance, validated_data):
        tracks_data = validated_data.pop('tracks')
        super(self.__class__, self).update(instance, validated_data)
        if tracks_data:
            track_to_delete = instance.tracks.exclude(pk__in=[item.get('id', None) for item in tracks_data])

            for item in tracks_data:
                item_id = item.get('id', None)
                if item_id:
                    track_item = Track.objects.get(id=item_id, album=instance)
                    track_item.title = item.get('title', track_item.title)
                    track_item.save()
                else:
                    Track.objects.create(album=instance, **item)
        else:
            track_to_delete = instance.tracks.all()
        # Delete tracks which are not exists in validated_data
        if track_to_delete:
            track_to_delete.delete()
        return instance
