#!/usr/bin/env python
# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FieldWithButtons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms
from django.urls import reverse


class SearchForm(forms.Form):
    query = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_action = reverse('albums:list')
        self.helper.form_class = 'navbar-form navbar-left'
        self.helper.attrs = {'role': 'search'}
        self.helper.form_method = 'GET'
        self.helper.layout = Layout(FieldWithButtons(Field('query', autofocus='autofocus'), Submit('', 'Search')))
