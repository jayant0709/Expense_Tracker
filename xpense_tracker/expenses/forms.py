# forms.py
from django import forms
from .models import Expense



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'category', 'date', 'amount']

from .models import Income
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'date']
