#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def query_builder(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if ('page' == k and isinstance(v, int) and int(v) > 1) or ('page' != k and v is not None):
            updated[k] = v
        else:
            updated.pop(k, 0)  # Remove or return 0 - aka, delete safely this key
    return f'?{updated.urlencode()}' if updated else ''
