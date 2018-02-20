#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from album.models import Album
from track.models import Track
from track.serializers import TrackUpdateSerializer


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'tracks')

    tracks = TrackUpdateSerializer(many=True)

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks', None)
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album

    def update(self, instance, validated_data):
        if 'tracks' in validated_data:
            tracks_data = validated_data.pop('tracks', None)
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

        super(AlbumSerializer, self).update(instance, validated_data)
        return instance
