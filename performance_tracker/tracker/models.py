
from django.db import models
from django.contrib.auth.models import User

class PerformanceData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    income = models.FloatField()
    expenses = models.FloatField()
    profit = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        # Automatically calculate profit
        self.profit = self.income - self.expenses
        super(PerformanceData, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.date}'
    

    class Expense(models.Model):
      amount = models.DecimalField(max_digits=10, decimal_places=2)
      category = models.CharField(max_length=50)  # Rent, Utilities, etc.
      description = models.TextField()

    def __str__(self):
        return self.category





