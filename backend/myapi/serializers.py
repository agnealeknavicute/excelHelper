from .models import Income, Expense
from rest_framework import serializers


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['name', 'income']

class UpdatedIncomeListSerializer(serializers.ListSerializer):
    child = IncomeSerializer()

class UpdatedIncomeSerializer(serializers.Serializer):
    incomeItems = UpdatedIncomeListSerializer()

    def create(self, validated_data):
        income_items_data = validated_data.get('incomeItems')
        income_items = [Income.objects.create(**item) for item in income_items_data]
        return {'incomeItems': income_items}

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Expense
        fields= '__all__'