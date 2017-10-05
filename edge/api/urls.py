# -*- coding: utf-8 -*-
from django.conf.urls import url
from .controllers import students_controller
from .controllers import discipline_controller

urlpatterns = [
	# Resource STUDENTS
	url(
        r'^api/v1/students/(?P<pk>[0-9]+)$',
        students_controller.get_delete_update_students,
        name='get_delete_update_students'
    ),
    url(
        r'^api/v1/students/$',
        students_controller.get_post_students,
        name='get_post_students'
    ),

	# Resource subjects
	url(
        r'^api/v1/subjects/(?P<pk>[0-9]+)$',
        discipline_controller.get_delete_update_discipline,
        name='get_delete_update_students'
    ),
    url(
        r'^api/v1/subjects/$',
        discipline_controller.get_post_discipline,
        name='get_post_students'
    ),
	url(
        r'^api/v1/subjects/add_schedule$',
        discipline_controller.add_schedule,
        name='get_post_students'
    ),
	url(
        r'^api/v1/subjects/(?P<pk>[0-9]+)/view_schedules$',
        discipline_controller.view_schedules,
        name='get_post_students'
    )
]
