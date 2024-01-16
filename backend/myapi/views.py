from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from openpyxl import Workbook
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from myapi.models import Income
from myapi.serializers import UpdatedIncomeSerializer


class IncomeApi(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = UpdatedIncomeSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Создание таблицы в Excel
        df = pd.DataFrame([serializer.data])
        excel_file_path = 'income_data.xlsx'
        df.to_excel(excel_file_path, index=False, engine='openpyxl')

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

        # Создание таблицы в Excel
        df = pd.DataFrame([serializer.data])
        excel_file_path = 'expense_data.xlsx'
        df.to_excel(excel_file_path, index=False, engine='openpyxl')

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()