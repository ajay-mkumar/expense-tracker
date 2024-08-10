from django import forms
from ..models import Expense


class ExpenseForm(forms.ModelForm):
    spent_date = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = Expense
        fields = ['expenses', 'amount_spent', 'spent_date']
