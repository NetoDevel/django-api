# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import RegistryStudent
from ..serializers import RegistryStudentSerializer
from rest_framework.parsers import JSONParser
import json

@api_view(['POST'])
def post_registry_student(request):
    data = {
        'discipline_id': request.data.get('registry')['discipline_id'],
        'student_id': request.data.get('registry')['student_id']
    }

    registry = RegistryStudent(discipline_id=data['discipline_id'], student_id=data['student_id'])
    registry.save()

    serializer = RegistryStudentSerializer(registry)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
