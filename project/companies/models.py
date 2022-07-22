from django.db import models
from django.utils import timezone
from django.contrib import admin
import datetime
# Create your models here.
class Companies(models.Model):
    companies_num= models.IntegerField(2)
    pub_date= models.DateTimeField('date published')
    def __int__(self): 
        return self.companies_num
    @admin.display(
        boolean= True,
        ordering='pub_date',
        description='Published recently'
    )
    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date<=now
        
class Employees(models.Model):
    companies= models.ForeignKey(Companies, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
    def __str__(self): 
        return self.first_name
    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1)<=self.pub_date<=now