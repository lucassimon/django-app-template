# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# Third-party app imports

# Imports from your apps


urlpatterns = patterns(
    '{{ app_name }}.views',
    url(r'^$', 'homepage', name='homepage'),
)
