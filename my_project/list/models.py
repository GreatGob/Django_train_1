from django.db import models
from django.contrib import admin
from django.utils import timezone
import datetime
# Create your models here.

class Companies(models.Model):
    company_name= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
    def __str__(self):
        return f"Company: {self.company_name}"
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='published recently',
    )
    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date<=now
    
class Employees(models.Model):
    company= models.ForeignKey(Companies, related_name='employee', on_delete= models.CASCADE)
    employee_name= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
    def __str__(self):
        return f"Name: {self.employee_name}"
    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date<=now
    
class Details(models.Model):
    employee= models.ForeignKey(Employees, on_delete=models.CASCADE)
    full_name= models.CharField(max_length=200)
    age= models.IntegerField()
    pub_date= models.DateTimeField('date published')
    def __str__(self):
        return f"Name: {self.full_name} and age:{self.age}"
    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date<=now