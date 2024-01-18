from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openpyxl
from openpyxl.styles import Alignment
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from myapi.models import IncExpModel
from myapi.serializers import UpdatedIncomeSerializer
from rest_framework import serializers
from django.http import FileResponse
from django.views import View
from django.http import FileResponse
import os

class ExcelDownloadView(View):
    def get(self, request, *args, **kwargs):
        excel_file_path = 'income_expense_data.xlsx'

        if os.path.exists(excel_file_path):
            book = openpyxl.load_workbook(excel_file_path)

            sheet_name = 'Sheet'
            if sheet_name in book.sheetnames:
                sheet = book[sheet_name]
                book.remove(sheet)

            book.save(excel_file_path)

            file = open(excel_file_path, 'rb')
            response = FileResponse(file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="example.xlsx"'
            return response
        else:
            return HttpResponseNotFound('File not found')


class ExcelManager:
    @staticmethod
    def create_or_load_excel(excel_file_path, sheet_name):
        try:
            book = openpyxl.load_workbook(excel_file_path)
            if sheet_name not in book.sheetnames:
                book.create_sheet(sheet_name)
                book.save(excel_file_path)
        except FileNotFoundError:
            book = openpyxl.Workbook()
            book.save(excel_file_path)
            book.create_sheet(sheet_name)
            book.save(excel_file_path)

        sheet = book[sheet_name]
        return sheet

    @staticmethod
    def clear_existing_data(existing_sheet):
        existing_sheet.delete_rows(2, existing_sheet.max_row)

    @staticmethod
    def write_to_excel(existing_sheet, new_data, sheet_name, excel_file_path):
        if not existing_sheet['A1'].value or 'name' not in existing_sheet['A1'].value:
            existing_sheet.insert_cols(1)
            existing_sheet['A1'] = 'name'
        if not existing_sheet['B1'].value or 'value' not in existing_sheet['B1'].value:
            existing_sheet.insert_cols(2)
            existing_sheet['B1'] = 'value'
        if not existing_sheet['C1'].value or 'total' not in existing_sheet['C1'].value:
            existing_sheet.insert_cols(3)
            existing_sheet['C1'] = 'total'

        name_column_index = existing_sheet['A1'].column
        value_column_index = existing_sheet['B1'].column
        total_column_index = existing_sheet['C1'].column

        ExcelManager.clear_existing_data(existing_sheet)

        total_sum = 0  
        for row in new_data:
            name, value = row.get('name'), row.get('value')
            total_sum += float(value) 
            existing_sheet.append([name, value, None])  

        existing_sheet.cell(row=2, column=total_column_index, value=total_sum)

        book = existing_sheet.parent
        book.save(excel_file_path)

class IncExpApi(viewsets.ModelViewSet):
    queryset = IncExpModel.objects.all()
    serializer_class = UpdatedIncomeSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        data_list = serializer.validated_data.get('incomeItems', [])
        if data_list:
            new_data = [{'name': item['name'], 'value': item['value']} for item in data_list]

            excel_file_path = 'income_expense_data.xlsx'
            sheet_name = 'Incomes'

            existing_sheet = ExcelManager.create_or_load_excel(excel_file_path, sheet_name)

            ExcelManager.write_to_excel(existing_sheet, new_data, sheet_name, excel_file_path)
        else:
            data_list = serializer.validated_data.get('expenseItems', [])
            new_data = [{'name': item['name'], 'value': item['value']} for item in data_list]

            excel_file_path = 'income_expense_data.xlsx'
            sheet_name = 'Expenses'

            existing_sheet = ExcelManager.create_or_load_excel(excel_file_path, sheet_name)

            ExcelManager.write_to_excel(existing_sheet, new_data, sheet_name, excel_file_path)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        

    def perform_create(self, serializer):
        serializer.save()
