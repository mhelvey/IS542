#!/usr/bin/env python3
import os

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django
django.setup()

# import models and run django/python commands
from homepage import models as hmod


# 1. Print the names and emails of all the students in your database, in alphabetical order by email.
print("1. Print Names and emails, ordered alphabetically by email")
students = hmod.Student.objects.all().order_by('email')
for s in students:
    print("\tName: " + s.name)
    print("\tEmail: " + s.email + "\n")


# 2. Pick a single seminar (course) based on its unique seminar number.
# Be sure to wrap your call in a try/except Seminar.DoesNotExist block.  Print the seminar name and fees.
print("2. Pick a seminar based on it's unique seminar number. Print the name and fees.")
try:
    seminar = hmod.Seminar.objects.get(seminar_num=1)
    print("\tSeminar name: " + seminar.name)
    print("\tSeminar fees: $" + str(seminar.fees) + "\n")
except hmod.Seminar.DoesNotExist:
    print("Seminar doesn't exist")


# 3. Using the object you queried in #2, print the student name and marks received for those enrolled in the class.
print("3. Print student names and marks for those enrolled in object queried in #2")
enrollments = hmod.Enrollment.objects.all().filter(seminar__seminar_num=1)
print("\tStudents enrolled for " + seminar.name + ":")
for e in enrollments:
    stud = str(e.student.name)
    print("\t\t-" + stud + ": " + str(e.marks_received))


# 4. Using the object you queried in #2, print the professor’s name that teaches it.
print("\n4. Print teacher name from object queried in #2")
teacher = seminar.professor.name
print("\t" + teacher + " is the professor for " + seminar.name)


# 5. Using the object you queried in #2, print the names of the students on the waiting list.
print("\n5. Print student names of those on waiting list for object queried in #2")
waiting = hmod.WaitingList.objects.all().filter(seminar__seminar_num=1)
print("\tStudents on the waiting list for " + seminar.name + ":")
for e in waiting:
    stud = str(e.student.name)
    print("\t\t-" + stud)


# 6. What is the average fee amount for courses with fees (don’t include courses without fees)?
#    What is the maximum fee?  What is the minimum (non-zero) fee?
print("\n6. Print average, max and min fees.")
seminars = hmod.Seminar.objects.all()
sum = 0
max = 0
min = 0
for s in seminars:
    if s.fees > 0:
        fee = s.fees
        sum = sum + fee
    if fee > max:
        max = fee
        min = max
    if fee < min:
        min = fee

average = float(sum/len(seminars))

print("\t Average:\t$" + str(average))
print("\t Maximum:\t$" + str(max))
print("\t Minimum:\t$" + str(min))


# 7. What seminars have no assigned teachers?  In other words, query the seminar table where the professor
# foreign key is null. Django has a special way to query null values, so be sure to use it.
# Null values are not empty strings.
print("\n7. Print the seminars that do not have a professor.")
seminars = hmod.Seminar.objects.all().filter(professor__isnull=True)
for s in seminars:
    print("\t-" + s.name)


# 8. Print the names and addresses of students who live in Provo.
# In other words, query students where the address field contains the word “Provo”.
students = hmod.Student.objects.all().filter(address__contains="Provo")
print("\n8. Print all students that live in Provo.")
for s in students:
    print("\tName:\t " + s.name)
    print("\tAddress: " + s.address + "\n")


# 9. Print the total number of students, seminars, and professors in our database using Django’s count() method.
print("9. Print the total number of students, seminars, and professors.")
num_students = hmod.Student.objects.all().count()
num_profs = hmod.Professor.objects.all().count()
num_seminars = hmod.Seminar.objects.all().count()
print("\tNumber of Students:\t" + str(num_students))
print("\tNumber of Professors:\t" + str(num_profs))
print("\tNumber of Seminars\t" + str(num_seminars))
