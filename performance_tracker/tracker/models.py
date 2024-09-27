
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