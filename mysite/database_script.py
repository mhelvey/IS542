#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

# import models and run django/python commands
from homepage import models as hmod
try:
    professor = hmod.Professor.objects.get(email='yoda@jedi.com')
    print("Professor " + professor.name + " already exists")
except hmod.Professor.DoesNotExist:
    professor = hmod.Professor()
    professor.name = "Yoda"
    professor.address = "Degobah"
    professor.email = "yoda@jedi.com"
    professor.phone = "1234567890"
    professor.salary = 100000
    professor.save()
    print("Professor " + professor.name + " created")

try:
    professor = hmod.Professor.objects.get(email='obi@jedi.com')
    print("Professor " + professor.name + " already exists")
except hmod.Professor.DoesNotExist:
    professor = hmod.Professor()
    professor.name = "Obi-Wan"
    professor.address = "Tatooine"
    professor.email = "obi@jedi.com"
    professor.phone = "0123456789"
    professor.salary = 75000
    professor.save()
    print("Professor " + professor.name + " created")

try:
    student = hmod.Student.objects.get(email='luke@jedi.com')
    print("Student " + student.name + " already exists")
except hmod.Student.DoesNotExist:
    student = hmod.Student()
    student.name = "Luke Skywalker"
    student.address = "Tatooine"
    student.email = "luke@jedi.com"
    student.phone = "2345678901"
    student.student_num = '12345'
    student.average_mark = 3.85
    student.save()
    print("Student " + student.name + " created")

try:
    student = hmod.Student.objects.get(email='han@jedi.com')
    print("Student " + student.name + " already exists")
except hmod.Student.DoesNotExist:
    student = hmod.Student()
    student.name = "Han Solo"
    student.address = "Corellia"
    student.email = "han@jedi.com"
    student.phone = "3456789012"
    student.student_num = '23456'
    student.average_mark = 3.35
    student.save()
    print("Student " + student.name + " created")

try:
    student = hmod.Student.objects.get(email='leia@jedi.com')
    print("Student " + student.name + " already exists")
except hmod.Student.DoesNotExist:
    student = hmod.Student()
    student.name = "Leia Organa"
    student.address = "Alderaan"
    student.email = "leia@jedi.com"
    student.phone = "4567890123"
    student.student_num = '34567'
    student.average_mark = 4.0
    student.save()
    print("Student " + student.name + " created")

try:
    student = hmod.Student.objects.get(email='michael@jedi.com')
    print("Student " + student.name + " already exists")
except hmod.Student.DoesNotExist:
    student = hmod.Student()
    student.name = "Michael"
    student.address = "7201 University Station, Provo UT"
    student.email = "michael@jedi.com"
    student.phone = "4567890123"
    student.student_num = '45678'
    student.average_mark = 4.0
    student.save()
    print("Student " + student.name + " created")

try:
    student = hmod.Student.objects.get(email='cameron@jedi.com')
    print("Student " + student.name + " already exists")
except hmod.Student.DoesNotExist:
    student = hmod.Student()
    student.name = "Cameron"
    student.address = "11029 Bulldog Ave, Provo UT"
    student.email = "cameron@jedi.com"
    student.phone = "4567890123"
    student.student_num = '56789'
    student.average_mark = 4.0
    student.save()
    print("Student " + student.name + " created")

try:
    seminar = hmod.Seminar.objects.get(seminar_num=1)
    print(seminar.name + " Seminar already exists")
except hmod.Seminar.DoesNotExist:
    seminar = hmod.Seminar()
    seminar.name = "Lifting X-Wing"
    seminar.seminar_num = 1
    seminar.fees = 100
    seminar.professor = hmod.Professor.objects.get(name="Yoda")
    seminar.save()
    print(seminar.name + " Seminar created")

try:
    seminar = hmod.Seminar.objects.get(seminar_num=2)
    print(seminar.name + " Seminar already exists")
except hmod.Seminar.DoesNotExist:
    seminar = hmod.Seminar()
    seminar.name = "Force Mind Control 101"
    seminar.seminar_num = 2
    seminar.fees = 100
    seminar.professor = hmod.Professor.objects.get(name="Obi-Wan")
    seminar.save()
    print(seminar.name + " Seminar created")

try:
    seminar = hmod.Seminar.objects.get(seminar_num=3)
    print(seminar.name + " Seminar already exists")
except hmod.Seminar.DoesNotExist:
    seminar = hmod.Seminar()
    seminar.name = "Force Choke 101"
    seminar.seminar_num = 3
    seminar.fees = 1
    seminar.save()
    print(seminar.name + " Seminar created")

try:
    seminar = hmod.Seminar.objects.get(seminar_num=4)
    print(seminar.name + " Seminar already exists")
except hmod.Seminar.DoesNotExist:
    seminar = hmod.Seminar()
    seminar.name = "Wookie Roar 101"
    seminar.seminar_num = 4
    seminar.fees = 0
    seminar.save()
    print(seminar.name + " Seminar created")

try:
    enrollment = hmod.Enrollment.objects.get(student=hmod.Student.objects.get(name='Luke Skywalker'),
                      seminar=hmod.Seminar.objects.get(seminar_num=1))
    print(enrollment.student.name + " is already enrolled in " + enrollment.seminar.name)
except hmod.Enrollment.DoesNotExist:
    enrollment = hmod.Enrollment()
    enrollment.student = hmod.Student.objects.get(name='Luke Skywalker')
    enrollment.seminar = hmod.Seminar.objects.get(seminar_num=1)
    enrollment.marks_received = 4.0
    enrollment.save()
    print(enrollment.student.name + " is now enrolled in " + enrollment.seminar.name)

try:
    enrollment = hmod.Enrollment.objects.get(student=hmod.Student.objects.get(name='Han Solo'),
                      seminar=hmod.Seminar.objects.get(seminar_num=1))
    print(enrollment.student.name + " is already enrolled in " + enrollment.seminar.name)
except hmod.Enrollment.DoesNotExist:
    enrollment = hmod.Enrollment()
    enrollment.student = hmod.Student.objects.get(name='Han Solo')
    enrollment.seminar = hmod.Seminar.objects.get(seminar_num=1)
    enrollment.marks_received = 4.0
    enrollment.save()
    print(enrollment.student.name + " is now enrolled in " + enrollment.seminar.name)

try:
    enrollment = hmod.Enrollment.objects.get(student=hmod.Student.objects.get(name='Luke Skywalker'),
                      seminar=hmod.Seminar.objects.get(seminar_num=2))
    print(enrollment.student.name + " is already enrolled in " + enrollment.seminar.name)
except hmod.Enrollment.DoesNotExist:
    enrollment = hmod.Enrollment()
    enrollment.student = hmod.Student.objects.get(name='Luke Skywalker')
    enrollment.seminar = hmod.Seminar.objects.get(seminar_num=2)
    enrollment.marks_received = 4.0
    enrollment.save()
    print(enrollment.student.name + " is now enrolled in " + enrollment.seminar.name)

try:
    wait = hmod.WaitingList.objects.get(student=hmod.Student.objects.get(name='Han Solo'),
                      seminar=hmod.Seminar.objects.get(seminar_num=2))
    print(wait.student.name + " is already on the waiting list for " + wait.seminar.name)
except hmod.WaitingList.DoesNotExist:
    wait = hmod.WaitingList()
    wait.student = hmod.Student.objects.get(name='Han Solo')
    wait.seminar = hmod.Seminar.objects.get(seminar_num=2)
    wait.save()
    print(wait.student.name + " is now on the waiting list for " + wait.seminar.name)

try:
    wait = hmod.WaitingList.objects.get(student=hmod.Student.objects.get(name='Leia Organa'),
                      seminar=hmod.Seminar.objects.get(seminar_num=1))
    print(wait.student.name + " is already on the waiting list for " + wait.seminar.name)
except hmod.WaitingList.DoesNotExist:
    wait = hmod.WaitingList()
    wait.student = hmod.Student.objects.get(name='Leia Organa')
    wait.seminar = hmod.Seminar.objects.get(seminar_num=1)
    wait.save()
    print(wait.student.name + " is now on the waiting list for " + wait.seminar.name)