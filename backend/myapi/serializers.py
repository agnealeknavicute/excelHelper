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

# class ExpenseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Expense  # Define the Expense model
#         fields = ['name', 'value', 'type']

# class UpdatedExpenseListSerializer(serializers.ListSerializer):
#     child = ExpenseSerializer()

# # class UpdatedExpenseSerializer(serializers.Serializer):
# #     expenseItems = UpdatedExpenseListSerializer()

# class UpdatedExpenseSerializer(serializers.Serializer):
#     expenseItems = UpdatedExpenseListSerializer()

#     def create(self, validated_data):
#         expense_items_data = validated_data.get('expenseItems')
#         type_value = expense_items_data[0].get('type', 'expense')  # Assuming the 'type' is the same for all items

#         # Remove 'type' from the dictionary to avoid conflict
#         for item in expense_items_data:
#             item.pop('type', None)

#         expense_items = [Expense.objects.create(type=type_value, **item) for item in expense_items_data]
#         return {'expenseItems': expense_items}
