# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	registry = models.CharField("registry", max_length=255)
	name = models.CharField("name", max_length=255)
	period = models.CharField("period", max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Discipline(models.Model):
	name = models.CharField("name", max_length = 255)
	menu = models.CharField("menu", max_length = 255)
	code = models.IntegerField("code")
	work_load = models.IntegerField("work_load")

class DisciplineSchedule(models.Model):
	start_time = models.DateTimeField(name="start_time")
	end_time = models.DateTimeField(name="end_time")
	day = models.CharField(name="day", max_length = 10)
	discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE)

class RegistryStudent(models.Model):
	student = models.ForeignKey(Student, on_delete = models.CASCADE)
	discipline = models.ForeignKey(Discipline, on_delete = models.CASCADE)
