from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from myapi.models import Income
from myapi.serializers import UpdatedIncomeSerializer

a=10
class IncomeApi(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = UpdatedIncomeSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Преобразование данных сериализатора в словарь
        data_list = serializer.validated_data['incomeItems']

        # Создание DataFrame из новых данных
        new_df = pd.DataFrame(data_list)

        # Путь к файлу Excel
        excel_file_path = 'income_data.xlsx'

        # Если файл не существует, создаем новый
        try:
            existing_df = pd.read_excel(excel_file_path, engine='openpyxl')
        except Exception as e:
            print(f"Error reading existing file: {e}")
            existing_df = pd.DataFrame()
            existing_df.to_excel(excel_file_path, index=False, engine='openpyxl')
            print(f"Created a new file: {excel_file_path}")

        # Объединение существующего DataFrame с новым
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Сохранение обновленного DataFrame в Excel
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            try:
                # Попытка записи в существующий лист 'Incomes'
                updated_df.to_excel(writer, index=False, sheet_name='Incomes')
            except ValueError:
                # Если лист существует, то записываем в него
                writer.book = openpyxl.load_workbook(excel_file_path)
                writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
                sheet_name = 'Incomes' if 'Incomes' in writer.sheets else None
                updated_df.to_excel(writer, index=False, sheet_name=sheet_name)

                a = a+10
                # Получение ссылки на лист 'Incomes'
                sheet = writer.sheets[str(a)]

                # Добавление заголовка над таблицей
                title_cell = sheet.cell(row=1, column=1, value='INCOMES')
                title_cell.alignment = Alignment(horizontal='center')
                

                # Добавление названий колонок под заголовком
                for col_num, value in enumerate(updated_df.columns.values, start=1):
                    col_name_cell = sheet.cell(row=2, column=col_num, value=value)
                    col_name_cell.alignment = Alignment(horizontal='center')

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()










  



class ExpenseApi(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = UpdatedIncomeSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Преобразование данных сериализатора в словарь
        data_list = serializer.validated_data['incomeItems']

        # Чтение существующего файла Excel или создание нового, если файла нет
        excel_file_path = 'expense_data.xlsx'
        try:
            existing_df = pd.read_excel(excel_file_path, engine='openpyxl')
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Создание DataFrame из новых данных
        new_df = pd.DataFrame(data_list)

        # Объединение существующего DataFrame с новым
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Сохранение обновленного DataFrame в Excel
        updated_df.to_excel(excel_file_path, index=False, engine='openpyxl')

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
