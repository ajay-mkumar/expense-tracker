import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense(models.Model):
    expense_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    expenses = models.CharField(max_length=500)
    amount_spent = models.FloatField()
    spent_date = models.DateField()
    
