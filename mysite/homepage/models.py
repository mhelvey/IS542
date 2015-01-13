from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200, unique=True)
    address = models.TextField(max_length=500)
    phone = models.TextField(max_length=15)
    email = models.EmailField(max_length=254)
    student_num = models.TextField(max_length=30)
    average_mark = models.DecimalField(max_digits=7, decimal_places=2)

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200, unique=True)
    address = models.TextField(max_length=500)
    phone = models.TextField(max_length=15)
    email = models.EmailField(max_length=254)
    salary = models.DecimalField(max_digits=9, decimal_places=2)

class Seminar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200, unique=True)
    seminar_num = models.TextField(max_length=30)
    fees = models.DecimalField(max_digits=7, decimal_places=2)
    professor = models.ForeignKey(to=Professor, to_field='name', blank=True)

class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    marks_received = models.DecimalField(max_digits=7, decimal_places=2)
    student = models.ForeignKey(to=Student, to_field='name', blank=False)
    seminar = models.ForeignKey(to=Seminar, to_field='name', blank=False)

class WaitingList(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(to=Student, to_field='name', blank=False)
    seminar = models.ForeignKey(to=Seminar, to_field='name', blank=False)

