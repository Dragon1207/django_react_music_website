#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def query_builder(request, **kwargs):
    updated = request.GET.copy()
    for k, value in kwargs.items():
        if (k == 'page' and isinstance(value, int) and int(value) > 1) or (k != 'page' and value is not None):
            updated[k] = value
        else:
            updated.pop(k, 0)  # Remove or return 0 - aka, delete safely this key
    return f'?{updated.urlencode()}' if updated else ''
