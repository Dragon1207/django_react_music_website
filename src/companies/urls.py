#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.StockList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
