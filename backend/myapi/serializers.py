from .models import Income, Expense
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Income
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Expense
        fields= '__all__'