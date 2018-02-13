from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class University(models.Model):
	name = models.CharField(verbose_name='University Name', max_length = 50)
	logo = models.ImageField(upload_to = 'university_logo/',)
	website = models.CharField(max_length = 50, null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = "University"
		verbose_name_plural = "University"

	def __str__(self):
		return self.name


class School(models.Model):
	owner = models.ForeignKey(User)
	university = models.ForeignKey(University,  related_name='schools')
	name = models.CharField(verbose_name='School Name', max_length = 50)
	logo = models.ImageField(upload_to = 'school_logo/', null=True, blank=True)
	website = models.CharField(max_length = 50, null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = "School"
		verbose_name_plural = "School"

	def __str__(self):
		return self.name


class Address(models.Model):
	country = (
		('india','India'),
		('england','England'),
		('australia','Australia'),
		('united_states','United States'),
		('canada','Canada'),
		('new_zealand','New Zealand'),
		)

	address1 = models.CharField(max_length = 50)
	address2 = models.CharField(max_length = 50)
	city = models.CharField(max_length = 15)
	state = models.CharField(max_length = 15)
	country = models.CharField(choices=country, max_length = 15)
	zipcode = models.IntegerField(null=True, blank=True)
	mobile = models.BigIntegerField(verbose_name='Mobile No.', max_length = 13, null=True, blank=True)

	class Meta:
		verbose_name = "Address"
		verbose_name_plural = "Address"

	def __str__(self):
		return self.city


class Student(models.Model):
	school = models.ForeignKey(School)
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	roll_no = models.IntegerField()
	email = models.EmailField()
	date_of_birth = models.CharField(max_length = 10)
	address =  models.ManyToManyField(Address)
	SMARTNumber = models.CharField(max_length = 25, null=True, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Student"
		verbose_name_plural = "Student"

	def __str__(self):
		return self.first_name