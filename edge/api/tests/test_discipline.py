import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Discipline
from ..serializers import DisciplineSerializer

client = Client()

class GetAllDisciplineTest(TestCase):
    def setUp(self):
        Discipline.objects.create(name='java', menu='0001', code=1, work_load=8)
        Discipline.objects.create(name='python', menu='0001', code=1, work_load=8)

    def test_get_all_puppies(self):
        response = client.get(reverse('get_post_discipline'))
        discipline = Discipline.objects.all()
        serializer = DisciplineSerializer(discipline, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
