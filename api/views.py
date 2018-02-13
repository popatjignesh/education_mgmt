from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from school_mgmt.serializers import *
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from school_mgmt.models import *
from random import randint


@api_view(['POST'])
def register(request):
	serializer = UserSerializer(data=request.data)
	psw1 = request.data['password']
	psw2 = request.data['confirm_password']
	if psw1 == psw2:
		if serializer.is_valid():
			obj = serializer.save()
			obj.set_password(request.data['password'])
			obj.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def university_list(request):
	universities = University.objects.all()
	serializer = UniversitySerializer(universities, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def school_add(request):
	if request.user.is_authenticated():
		owner = request.user
		data = request.data
		data['owner'] = owner.id
		serializer = SchoolSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_list(request):
	if request.user.is_authenticated():
		schools = School.objects.filter(owner=request.user)
		serializer = SchoolSerializer(schools, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_detail(request, pk):
	if request.user.is_authenticated():
		try:
			owner = request.user
			school = School.objects.get(id=pk, owner=owner)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)
		serializer = SchoolSerializer(school, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def school_update(request, pk):
	if request.user.is_authenticated():
		try:
			school = School.objects.get(id=pk)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

		owner = request.user
		data = request.data
		data['owner'] = owner.id

		serializer = SchoolSerializer(school, data=data, many=False)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def school_delete(request, pk):
	if request.user.is_authenticated():
		try:
			school = School.objects.get(id=pk)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)
		school.delete()
		return Response({'success': 'School deleted successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def university_list1(request):
	universities = University.objects.all()
	serializer = UniversitySerializer1(universities, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def student_add(request):
	data = request.data

	one = str(randint(1000, 9999))

	dob = request.data['date_of_birth']
	two = dob[0:2]
	five = dob[3:5]
	six = dob[6:10]

	s_id = request.data['school']
	school = str(School.objects.get(id=s_id))
	university = str(University.objects.get(schools__id=s_id))
	three = university[0:3].upper()
	four = school[0:3].upper()

	smart_no = one + two + "-" + three + four + "-" + five + six

	data['SMARTNumber'] = smart_no

	serializer = StudentSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def university_delete(request, pk):
	try:
		university = University.objects.get(id=pk)
	except:
		return Response({'error': 'university id not found'}, status=status.HTTP_400_BAD_REQUEST)
	university.delete()
	return Response({'success': 'university deleted successfully'}, status=status.HTTP_200_OK)

