#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from taggit_selectize.widgets import TagSelectize

from album.models import Album


class AlbumFavoriteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super(AlbumFavoriteForm, self).__init__(*args, **kwargs)
        if instance is None:
            # if we didn't get an instance, instantiate a new one
            self.instance = Album()
        else:
            self.instance = instance
            choices = (item for item in instance.tracks.values_list('pk', 'title'))
            self.fields['favorite_track'] = \
                forms.TypedChoiceField(choices=choices, widget=forms.RadioSelect, coerce=int)

    def save(self):
        if self.errors:
            raise ValueError("The AlbumFavoriteForm could not be saved because the data didn't validate.")
        self.instance.set_favorite_track(self.cleaned_data['favorite_track'])


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'genre', 'album_logo', 'tags')
        widgets = {
            'tags': TagSelectize(),
        }

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout('artist', 'title', 'genre', 'album_logo', 'tags',
                                    FormActions(Submit('submit', 'Submit')))
