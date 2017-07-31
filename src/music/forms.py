#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import RadioSelect
from music.models import Album, Song


class AlbumFavoriteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(AlbumFavoriteForm, self).__init__(*args, **kwargs)
        if instance is None:
            # if we didn't get an instance, instantiate a new one
            self.instance = Album()
        else:
            self.instance = instance
            choices = (item for item in instance.songs.values_list('pk', 'song_title'))
            self.fields['favorite_song'] = forms.TypedChoiceField(choices=choices, widget=forms.RadioSelect, coerce=int)

    def save(self):
        if self.errors:
            raise ValueError(
                "The AlbumFavoriteForm could not be saved because the data didn't validate."
            )
        self.instance.set_favorite_song(self.cleaned_data['favorite_song'])
