# -*- coding: utf-8 -*-
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Student
from ..serializers import StudentSerializer

# initialize the APIClient app
client = Client()

class GetAllStudentTest(TestCase):

	def setUp(self):
		Student.objects.create(name='Neto', registry= '001', period = '1')
		Student.objects.create(name='Bruno', registry= '002', period = '2')

	def test_get_all_students(self):
		response = client.get(reverse('index'))

		students = Student.objects.all()
		serializer = StudentSerializer(students, many = True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
