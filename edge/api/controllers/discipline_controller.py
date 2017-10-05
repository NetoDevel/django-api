# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Discipline
from ..models import DisciplineSchedule
from ..serializers import DisciplineSerializer
from ..serializers import DisciplineScheduleSerializer
from rest_framework.parsers import JSONParser
import json

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_discipline(request, pk):
    try:
        discipline = Discipline.objects.get(pk=pk)
    except Discipline.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        discipline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        data = {
            'name': request.data.get('discipline')['name'],
            'menu': request.data.get('discipline')['menu'],
            'code': request.data.get('discipline')['code'],
            'work_load': request.data.get('discipline')['work_load']
        }
        serializer = DisciplineSerializer(discipline, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_discipline(request):
    if request.method == 'GET':
        discipline = Discipline.objects.all()
        serializer = DisciplineSerializer(discipline, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('discipline')['name'],
            'menu': request.data.get('discipline')['menu'],
            'code': request.data.get('discipline')['code'],
            'work_load': request.data.get('discipline')['work_load']
        }
        serializer = DisciplineSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_schedule(request):
    data = {
        'start_time': request.data.get('schedule')['start_time'],
        'end_time': request.data.get('schedule')['end_time'],
        'day': request.data.get('schedule')['day'],
        'discipline_id' : request.data.get('schedule')['discipline_id']
    }

    discipline_id = request.data.get('schedule')['discipline_id']
    discipline = Discipline.objects.get(pk = discipline_id)

    discipline_schedule = DisciplineSchedule(start_time = data['start_time'],
    end_time = data['end_time'], day = data['day'], discipline = discipline)

    discipline_schedule.save()

    return Response("success")

@api_view(['GET'])
def view_schedules(request, pk):
    schedules = DisciplineSchedule.objects.filter(discipline_id = pk)
    serializer = DisciplineScheduleSerializer(schedules, many = True)
    return Response(serializer.data)
