from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapi.models import Income , Expense
from myapi.serializers import IncomeSerializer, ExpenseSerializer
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets




#_________________________api___________________________

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

class IncomeApi(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    http_method_names = ['GET', 'POST']
                         


class ExpenseApi(viewsets.ModelViewSet):
    queryset= Expense.objects.all()
    serializer_class = ExpenseSerializer
    http_method_names =['GET','POST']
