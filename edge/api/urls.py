# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^api/v1/students/(?P<pk>[0-9]+)$',
        views.get_delete_update_student,
        name='get_delete_update_student'
    ),
    url(
        r'^api/v1/students/$',
        views.index,
        name='index'
    )
]