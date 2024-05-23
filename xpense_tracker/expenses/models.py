from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Sum


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None) 
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_spendings = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)

    @classmethod
    def calculate_analysis(cls, user, start_date, end_date):
        analysis = {}
        expenses = cls.objects.filter(user=user, date__range=[start_date, end_date])

        # Calculate average expense
        total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] if expenses.exists() else 0
        total_days = (end_date - start_date).days if (end_date - start_date).days != 0 else 1  # Avoid division by zero
        analysis['average_expense'] = round(total_expense / total_days, 2)

        # Calculate daily average expense
        daily_avg_expense = expenses.aggregate(Avg('amount'))['amount__avg'] if expenses.exists() else 0
        analysis['daily_average_expense'] = round(daily_avg_expense, 2)

        max_expense = expenses.aggregate(Max('amount'))['amount__max']
        analysis['max_expense'] = max_expense
        max_expense_obj = expenses.filter(amount=max_expense).first()
        analysis['max_expense_day'] = max_expense_obj.date if max_expense_obj else None
        # analysis['max_expense_category'] = max_expense_obj.category if max_expense_obj else None
        analysis['max_expense_name'] = max_expense_obj.name if max_expense_obj else None

        return analysis


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, default='INR')  # Add currency field

    def __str__(self):
        return self.user.username

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
