from rest_framework import serializers
from .models import Student
from .models import Discipline
from .models import DisciplineSchedule

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('id', 'registry', 'name', 'period')

class DisciplineSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = Discipline
		fields = ('id', 'name', 'menu', 'code', 'work_load')

class DisciplineScheduleSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = DisciplineSchedule
		fields = ('id', 'start_time', 'end_time', 'day', 'discipline_id')
