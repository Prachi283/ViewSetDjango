from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	joining_date=models.DateField()
	emp_id=models.IntegerField()
