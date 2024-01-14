# Используйте
from django.urls.base import path, include
from . import views
from myapi.views import IncomeApi, ExpenseApi 
from django.contrib import admin
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'api/inc', IncomeApi)
router.register(r'api/exp', ExpenseApi)

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path ('', include (router.urls) )

]

