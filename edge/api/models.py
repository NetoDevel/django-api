# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	registry = models.CharField("registry", max_length=255)
	name = models.CharField("name", max_length=255)
	period = models.CharField("period", max_length=255)
		