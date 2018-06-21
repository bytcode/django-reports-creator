# -*- coding: utf-8 -*-
# try:
from django.conf.urls import url
# except ImportError:
#     from django.conf.urls.defaults import *

from reports_creator.views import report, report_list


urlpatterns = [
    url(r'^$', report_list, name='model_report_list'),
    url(r'^(?P<slug>[\w-]+)/$', report, name='model_report_view'),
]
