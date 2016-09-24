from __future__ import unicode_literals

from django.db import models

class student(models.Model):
	studentid	= models.IntegerField(unique=True)
	slug		= models.SlugField(unique=True)
	name		= models.CharField(max_length=50)
	def __str__(self):
		return self.name

class faculty(models.Model):
	facultyid	= models.IntegerField(unique=True)
	name		= models.CharField(max_length=50)
	def __str__(self):
		return self.name

class course(models.Model):
	courseid	= models.IntegerField(unique=True)
	slug		= models.SlugField(unique=True)
	name		= models.CharField(max_length=50)
	subject		= models.CharField(max_length=50)
	start_date	= models.DateField()
	end_date	= models.DateField()
	faculty_name	= models.OneToOneField(faculty)
	student_name	= models.ManyToManyField(student)
	def __str__(self):
		return self.name
