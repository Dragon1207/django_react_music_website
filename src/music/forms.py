#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FieldWithButtons, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms
from django.urls import reverse
from taggit_selectize.widgets import TagSelectize

from music.models import Album


class SearchForm(forms.Form):
    query = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_action = reverse('music:albums:list')
        self.helper.form_class = 'navbar-form navbar-left'
        self.helper.attrs = {'role': 'search'}
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(
            FieldWithButtons(
                Field('query', autofocus='autofocus'),
                Submit('', 'Search')
            )
        )


class AlbumFavoriteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(AlbumFavoriteForm, self).__init__(*args, **kwargs)
        if instance is None:
            # if we didn't get an instance, instantiate a new one
            self.instance = Album()
        else:
            self.instance = instance
            choices = (item for item in instance.songs.values_list('pk', 'title'))
            self.fields['favorite_song'] = forms.TypedChoiceField(choices=choices, widget=forms.RadioSelect, coerce=int)

    def save(self):
        if self.errors:
            raise ValueError(
                "The AlbumFavoriteForm could not be saved because the data didn't validate."
            )
        self.instance.set_favorite_song(self.cleaned_data['favorite_song'])


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist', 'title', 'genre', 'album_logo', 'tags')
        widgets = {'tags': TagSelectize(), }

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'artist', 'title', 'genre', 'album_logo', 'tags',
            FormActions(
                Submit('submit', 'Submit')
            )
        )
