#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from companies.views import StockList

urlpatterns = [
    url(r'^$', StockList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
