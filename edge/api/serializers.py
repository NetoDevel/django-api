from rest_framework import serializers
from .models import Student
from .models import Discipline

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = ('id', 'registry', 'name', 'period')

class DisciplineSerializer(serializers.ModelSerializer):
	class Meta(object):
		model = Discipline
		fields = ('id', 'name', 'menu', 'code', 'work_load')
