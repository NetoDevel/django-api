# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from models import Student

# Create your tests here.
class StudentTest(TestCase):

	def setUp(self):
		Student.objects.create(name='José Vieira', registry='001', period='1')

	def test_data_student(self):
		student_jose = Student.objects.get(name='José Vieira')
		
		self.assertEqual(student_jose.registry, '001')
		self.assertEqual(student_jose.period, '1')