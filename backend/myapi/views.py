from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapi.models import Income 
from myapi.serializers import UpdatedIncomeSerializer
from rest_framework import viewsets
from rest_framework import viewsets, permissions
from rest_framework import status



#_________________________api___________________________

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'message': 'Hello, world!'})

class IncomeApi(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = UpdatedIncomeSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
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
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()



    
    

