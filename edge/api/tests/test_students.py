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
		response = client.get(reverse('get_post_students'))

		students = Student.objects.all()
		serializer = StudentSerializer(students, many = True)

#		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

class ShowStudentTest(TestCase):

	def setUp(self):
		self.neto = Student.objects.create(name='Neto', registry= '001', period = '1')
		self.bruno = Student.objects.create(name='Bruno', registry= '002', period = '2')

	def test_should_get_student_with_id_1(self):
		response = client.get(
			reverse('get_delete_update_students', kwargs={'pk': self.neto.pk}))
		student = Student.objects.get(pk = self.neto.pk)

		serializer = StudentSerializer(student)

		print response.data

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_should_not_found_student(self):
		response = client.get(reverse('get_delete_update_students', kwargs={'pk': 999}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewStudentTest(TestCase):

    def setUp(self):
        self.student = {
            'name': 'Neto',
            'registry': '012',
            'period': '1'
        }

        self.invalid_payload = {
            'name': '',
            'registry': '',
            'period': '1'
        }

    def test_create_valid_student(self):
        response = client.post(
            reverse('get_post_students'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_students(self):
        response = client.post(
            reverse('get_post_students'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleStudentTest(TestCase):

    def setUp(self):
        self.neto = Student.objects.create(
            name='Neto', registry='012', period='2')

        self.valid_payload = {
            'name': 'Neto2',
            'registry': '012',
            'period': '5'
        }

        self.invalid_payload = {
            'name': 1,
            'registry': 1,
            'period': 1
        }

    def test_valid_update_student(self):
        response = client.put(
            reverse('get_delete_update_students', kwargs={'pk': self.neto.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DeleteSingleStudentTest(TestCase):

    def setUp(self):
        self.neto = Student.objects.create(
            name='Neto', registry='012', period='2')

    def test_valid_delete_student(self):
        response = client.delete(
            reverse('get_delete_update_students', kwargs={'pk': self.neto.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = client.delete(
            reverse('get_delete_update_students', kwargs={'pk': 9991}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
