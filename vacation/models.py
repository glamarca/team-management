from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

VACATION_TYPES = (
    ('L', 'Legal'),
    ('C', 'Compensation'),
    ('R', 'Recuperation'),
    ('X', 'Exceptional')
)


class Person(models.Model):
    last_name = models.CharField(max_length = 50, blank = False, null = False)

class Vacation(models.Model):

    person = models.ForeignKey(Person, null = False,on_delete=models.CASCADE,blank=False)
    vacation_type = models.CharField(max_length = 1, blank = False, null = False, choices = VACATION_TYPES, default = 'L')
    amount_of_days = models.IntegerField(blank=False, null=False)

class AccountStatus(models.Model):
    ACCOUNT_STATUSES = (
        ('A','Active'),
        ('P','Pending'),
        ('I','Inactive')
    )

    person = models.ForeignKey(Person, null = False,on_delete=models.CASCADE,blank=False)
    status = models.CharField(max_length = 1, blank = False, null = False, choices = ACCOUNT_STATUSES, default = 'I')

class DemandStatus(models.Model):
    DEMAND_STATUSES = (
        ('A','Accepted'),
        ('R','Refused'),
        ('P','Pending'),
    )

    person = models.ForeignKey(Person, null = False,on_delete=models.CASCADE,blank=False)
    demand = models.ForeignKey(Demand, null = False,on_delete=models.CASCADE,blank=False)
    status = models.CharField(max_length = 1, blank = False, null = False, choices = DEMAND_STATUSES, default = 'P')
    motivation = models.CharField(max_length = 255, blank = True, null = True)
    encoding_date = models.DateTimeField(default=models.DateTimeField(default=timezone.now))
    encoding_user = models.CharField(max_length = 255, blank = False, null = False)


class Demand(models.Model):
    person = models.ForeignKey(Person, null = False,on_delete=models.CASCADE,blank=False)
    vacation_type = models.CharField(max_length = 1, blank = False, null = False, choices = VACATION_TYPES, default = 'L')
    amount_of_days = models.IntegerField(blank=False, null=False)
    first_day = encoding_date = models.DateTimeField(null=False)
    last_day = encoding_date = models.DateTimeField(null=False)


class Task(models.Model):
    TASKS_TYPES = (
        ('V','Validate demand'),
        ('A','Activate User')
    )

    person = models.ForeignKey(Person, null = False,on_delete=models.CASCADE,blank=False)
    task_type = models.CharField(max_length = 1, blank = False, null = False, choices = TASKS_TYPES, default = 'V')