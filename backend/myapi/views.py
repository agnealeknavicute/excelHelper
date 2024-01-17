# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import pandas as pd
# import openpyxl
# from openpyxl.styles import Alignment
# from rest_framework import viewsets, permissions, status
# from rest_framework.response import Response
# from myapi.models import Income
# from myapi.serializers import UpdatedIncomeSerializer

# a=10
# class IncomeApi(viewsets.ModelViewSet):
#     queryset = Income.objects.all()
#     serializer_class = UpdatedIncomeSerializer
#     http_method_names = ['get', 'post']
#     permission_classes = [permissions.AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         # Преобразование данных сериализатора в словарь
#         data_list = serializer.validated_data['incomeItems']

#         # Создание DataFrame из новых данных
#         new_df = pd.DataFrame(data_list)

#         # Путь к файлу Excel
#         excel_file_path = 'income_data.xlsx'

#         # Если файл не существует, создаем новый
#         try:
#             existing_df = pd.read_excel(excel_file_path, engine='openpyxl')
#         except Exception as e:
#             print(f"Error reading existing file: {e}")
#             existing_df = pd.DataFrame()
#             existing_df.to_excel(excel_file_path, index=False, engine='openpyxl')
#             print(f"Created a new file: {excel_file_path}")

#         # Объединение существующего DataFrame с новым
#         updated_df = pd.concat([existing_df, new_df], ignore_index=True)

#         # Сохранение обновленного DataFrame в Excel
#         with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#             try:
#                 # Попытка записи в существующий лист 'Incomes'
#                 updated_df.to_excel(writer, index=False, sheet_name='Incomes')
#             except ValueError:
#                 # Если лист существует, то записываем в него
#                 writer.book = openpyxl.load_workbook(excel_file_path)
#                 writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
#                 sheet_name = 'Incomes' if 'Incomes' in writer.sheets else None
#                 updated_df.to_excel(writer, index=False, sheet_name=sheet_name)

#                 a = a+10
#                 # Получение ссылки на лист 'Incomes'
#                 sheet = writer.sheets[str(a)]

#                 # Добавление заголовка над таблицей
#                 title_cell = sheet.cell(row=1, column=1, value='INCOMES')
#                 title_cell.alignment = Alignment(horizontal='center')
                

#                 # Добавление названий колонок под заголовком
#                 for col_num, value in enumerate(updated_df.columns.values, start=1):
#                     col_name_cell = sheet.cell(row=2, column=col_num, value=value)
#                     col_name_cell.alignment = Alignment(horizontal='center')

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         serializer.save()










  



# class ExpenseApi(viewsets.ModelViewSet):
#     queryset = Income.objects.all()
#     serializer_class = UpdatedIncomeSerializer
#     http_method_names = ['get', 'post']
#     permission_classes = [permissions.AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         # Преобразование данных сериализатора в словарь
#         data_list = serializer.validated_data['incomeItems']

#         # Чтение существующего файла Excel или создание нового, если файла нет
#         excel_file_path = 'expense_data.xlsx'
#         try:
#             existing_df = pd.read_excel(excel_file_path, engine='openpyxl')
#         except FileNotFoundError:
#             existing_df = pd.DataFrame()

#         # Создание DataFrame из новых данных
#         new_df = pd.DataFrame(data_list)

#         # Объединение существующего DataFrame с новым
#         updated_df = pd.concat([existing_df, new_df], ignore_index=True)

#         # Сохранение обновленного DataFrame в Excel
#         updated_df.to_excel(excel_file_path, index=False, engine='openpyxl')

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         serializer.save()

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from myapi.models import Income, Expense
from myapi.serializers import UpdatedIncomeSerializer, UpdatedExpenseSerializer



class ExcelManager:
    @staticmethod
    def create_or_load_excel(excel_file_path, sheet_name):
        try:
            existing_df = pd.read_excel(excel_file_path, engine='openpyxl', sheet_name=sheet_name)
        except FileNotFoundError:
            existing_df = pd.DataFrame()
            existing_df.to_excel(excel_file_path, index=False, engine='openpyxl', sheet_name=sheet_name)
            print(f"Created a new file: {excel_file_path}")

        return existing_df

    @staticmethod
    def write_to_excel(writer, updated_df, sheet_name):
        try:
            if sheet_name in writer.sheets:
                writer.book = openpyxl.load_workbook(writer.path)
                writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
            updated_df.to_excel(writer, index=False, sheet_name=sheet_name)
        except Exception as e:
            print(f"Error writing to Excel file: {e}")



class IncomeApi(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = UpdatedIncomeSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data_list = serializer.validated_data['incomeItems']
        new_df = pd.DataFrame(data_list)

        excel_file_path = 'income_expense_data.xlsx'
        sheet_name = 'Incomes'

        try:
            # Try to read the existing Excel file
            existing_df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame with 'Incomes'
            existing_df = pd.DataFrame(columns=['name', 'value'])
            existing_df.loc[0] = ['Incomes', '']  # Add a row with 'Incomes'

        # Concatenate the existing DataFrame with the new data
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Write the updated DataFrame to the Excel file
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            updated_df.to_excel(writer, index=False, sheet_name=sheet_name)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save() 






from rest_framework import serializers

# class ExpenseApi(viewsets.ModelViewSet):
#     queryset = Expense.objects.all()
#     serializer_class = UpdatedExpenseSerializer
#     http_method_names = ['get', 'post']
#     permission_classes = [permissions.AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         data_list = serializer.validated_data['expenseItems']
#         new_df = pd.DataFrame(data_list)

#         excel_file_path = 'income_expense_data.xlsx'
#         sheet_name = 'Expenses'  # Use 'Expenses' instead of 'Sheet2'

#         try:
#             # Try to read the existing Excel file
#             existing_df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
#         except FileNotFoundError:
#             # If the file doesn't exist, create a new DataFrame with 'Expenses'
#             existing_df = pd.DataFrame(columns=['name', 'value'])
#             existing_df.loc[0] = ['Expenses', '']  # Add a row with 'Expenses'

#         # Concatenate the existing DataFrame with the new data
#         updated_df = pd.concat([existing_df, new_df], ignore_index=True)

#         # Write the updated DataFrame to the Excel file
#         with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
#             updated_df.to_excel(writer, index=False, sheet_name=sheet_name)

#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         serializer.save()

class ExpenseApi(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = UpdatedExpenseSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data_list = serializer.validated_data['expenseItems']
        new_df = pd.DataFrame(data_list)

        excel_file_path = 'income_expense_data.xlsx'
        sheet_name = 'Expenses'

        try:
            # Try to read the existing Excel file
            existing_df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        except FileNotFoundError:
            # If the file doesn't exist, create a new DataFrame with 'Expenses'
            existing_df = pd.DataFrame(columns=['name', 'value'])
            existing_df.loc[0] = ['Expenses', '']  # Add a row with 'Expenses'

        # Concatenate the existing DataFrame with the new data
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Write the updated DataFrame to the Excel file
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            ExcelManager.write_to_excel(writer, updated_df, sheet_name)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()



