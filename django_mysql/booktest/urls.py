# -*- coding: utf-8 -*-
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^addBook/$',views.addBook),
    url(r'^delBook/$',views.delBook)
]