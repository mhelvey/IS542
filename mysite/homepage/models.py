from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=500)
    phone = models.TextField(max_length=15)
    email = models.EmailField(max_length=254)
    student_num = models.TextField(max_length=30)
    average_mark = models.DecimalField(max_digits=7, decimal_places=2)

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=500)
    phone = models.TextField(max_length=15)
    email = models.EmailField(max_length=254)
    salary = models.DecimalField(max_digits=9, decimal_places=2)

class Seminar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    seminar_num = models.TextField(max_length=30)
    fees = models.DecimalField(max_digits=7, decimal_places=2)
    professor = models.ForeignKey(to=Professor, null=True)

class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    marks_received = models.DecimalField(max_digits=7, decimal_places=2)
    student = models.ForeignKey(to=Student, blank=False)
    seminar = models.ForeignKey(to=Seminar, blank=False)

class WaitingList(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(to=Student, blank=False)
    seminar = models.ForeignKey(to=Seminar, blank=False)


class GalleryImage(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.TextField(max_length=500)
    file_path = models.TextField(max_length=500)
    size = models.DecimalField(max_digits=7, decimal_places=2)
    mime_type = models.TextField(max_length=25)
    title = models.TextField(max_length=40)