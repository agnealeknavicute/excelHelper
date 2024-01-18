from .models import IncExpModel
from rest_framework import serializers
from rest_framework import serializers

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.CharField()
    type = serializers.ChoiceField(choices=['income', 'expense'])

class UpdatedIncomeSerializer(serializers.Serializer):
    incomeItems = ItemSerializer(many=True, required=False)
    expenseItems = ItemSerializer(many=True, required=False)

    def create(self, validated_data):
        income_items_data = validated_data.get('incomeItems', [])
        expense_items_data = validated_data.get('expenseItems', [])

        if income_items_data:
            item_type_value = income_items_data[0].get('type', 'income')
            for item in income_items_data:
                item.pop('type', None)
            income_objects = [IncExpModel.objects.create(type=item_type_value, **item) for item in income_items_data]
            return {'incomeItems': income_objects, 'expenseItems': []}

        elif expense_items_data:
            item_type_value = expense_items_data[0].get('type', 'expense')
            for item in expense_items_data:
                item.pop('type', None)
            expense_objects = [IncExpModel.objects.create(type=item_type_value, **item) for item in expense_items_data]
            return {'incomeItems': [], 'expenseItems': expense_objects}

        else:
            return {'incomeItems': [], 'expenseItems': []}

