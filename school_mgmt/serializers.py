from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from school_mgmt.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')


class UniversitySerializer(serializers.ModelSerializer):
    school_count = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ('id', 'name', 'logo', 'website', 'created_date', 'modified_date', 'is_active', 'school_count')

    def get_school_count(self, obj):
        return obj.schools.count()


class UniversitySerializer1(serializers.ModelSerializer):
    school_name = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ('id', 'name', 'school_name')

    def get_school_name(self, obj):
        return SchoolSerializer1(School.objects.filter(university__id=obj.id),many = True).data


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_date', 'modified_date')


class SchoolSerializer1(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'university')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('created_date', 'modified_date')
