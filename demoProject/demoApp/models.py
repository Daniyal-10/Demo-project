from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    id= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=20)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Employee(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=25)
    designation = models.CharField(max_length=25, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

#foreign Key:
class Department(models.Model):
    deparment_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=30)

class Employee_2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)


# Customer model for using a User (Foreign Key)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    contact = models.IntegerField()
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


        
# "first_name" ,'last_name', "username","password" ,"email"