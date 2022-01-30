from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.deletion import CASCADE
from datetime import date


# Create your models here.
class StudentAttend(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_name = models.CharField(max_length=100)
    attendence = models.CharField(max_length=1,default='A')
    roll_no = models.CharField(max_length=12)
    phone_no =models.CharField(max_length=10)
    email = models.EmailField()
    date = models.DateField(default=date.today)
    datetime = models.DateTimeField(auto_now_add=True)