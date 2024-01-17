from .models import Income
from rest_framework import serializers


# class IncomeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Income
#         fields = ['name', 'value']

# class UpdatedIncomeListSerializer(serializers.ListSerializer):
#     child = IncomeSerializer()

# class UpdatedIncomeSerializer(serializers.Serializer):
#     incomeItems = UpdatedIncomeListSerializer()

#     def create(self, validated_data):
#         income_items_data = validated_data.get('incomeItems')
#         income_items = [Income.objects.create(**item) for item in income_items_data]
#         return {'incomeItems': income_items}

# class IncomeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Income
#         fields = ['name', 'value', 'type']

# class UpdatedIncomeListSerializer(serializers.ListSerializer):
#     child = IncomeSerializer()

# class UpdatedIncomeSerializer(serializers.Serializer):
#     incomeItems = UpdatedIncomeListSerializer()
    

# class UpdatedExpenseSerializer(serializers.Serializer):
#     incomeItems = UpdatedExpenseListSerializer()

#     def create(self, validated_data):
#         income_items_data = validated_data.get('incomeItems')
#         type_value = income_items_data[0].get('type', 'income')  # Assuming the 'type' is the same for all items

#         # Remove 'type' from the dictionary to avoid conflict
#         for item in income_items_data:
#             item.pop('type', None)

#         income_items = [Income.objects.create(type=type_value, **item) for item in income_items_data]
#         return {'incomeItems': income_items}

# serializers.py

from rest_framework import serializers
from .models import Income, Expense  # Make sure to import Expense here

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['name', 'value', 'type']

class UpdatedIncomeListSerializer(serializers.ListSerializer):
    child = IncomeSerializer()

class UpdatedIncomeSerializer(serializers.Serializer):
    incomeItems = UpdatedIncomeListSerializer()

    def create(self, validated_data):
        income_items_data = validated_data.get('incomeItems', [])

        # Assuming the 'type' is the same for all items
        type_value = income_items_data[0].get('type', 'income')

        # Remove 'type' from the dictionary to avoid conflict
        for item in income_items_data:
            item.pop('type', None)

        income_items = [Income.objects.create(type=type_value, **item) for item in income_items_data]
        return {'incomeItems': income_items}


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense  # Define the Expense model
        fields = ['name', 'value', 'type']

class UpdatedExpenseListSerializer(serializers.ListSerializer):
    child = ExpenseSerializer()

# class UpdatedExpenseSerializer(serializers.Serializer):
#     expenseItems = UpdatedExpenseListSerializer()

class UpdatedExpenseSerializer(serializers.Serializer):
    expenseItems = UpdatedExpenseListSerializer()

    def create(self, validated_data):
        expense_items_data = validated_data.get('expenseItems')
        type_value = expense_items_data[0].get('type', 'expense')  # Assuming the 'type' is the same for all items

        # Remove 'type' from the dictionary to avoid conflict
        for item in expense_items_data:
            item.pop('type', None)

        expense_items = [Expense.objects.create(type=type_value, **item) for item in expense_items_data]
        return {'expenseItems': expense_items}
