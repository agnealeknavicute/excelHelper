# Используйте
from django.urls import path, include
from . import views
from myapi.views import IncExpApi, ExcelDownloadView
from django.contrib import admin
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'api/inc', IncExpApi),
# router.register(r'api/excelData', ExcelDownloadView)

urlpatterns = [
    # path('hello-world/', views.hello_world, name='hello_world'),
    path ('', include (router.urls) ),
    path('excelData/', ExcelDownloadView.as_view(), name='excel-download'),

]

