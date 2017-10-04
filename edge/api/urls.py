# -*- coding: utf-8 -*-
from django.conf.urls import url
from .controllers import students_controller

urlpatterns = [
	url(
        r'^api/v1/students/(?P<pk>[0-9]+)$',
        students_controller.get_delete_update_students,
        name='get_delete_update_students'
    ),

    url(
        r'^api/v1/students/$',
        students_controller.get_post_students,
        name='get_post_students'
    )
]