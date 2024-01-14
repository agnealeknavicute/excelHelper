from django.db import models

# Create your models here.


class Income(models.Model):
    name = models.CharField(max_length=10)
    # intro = models.TextField(max_length=50)
    info = models.TextField()
    # img_link= models.TextField()
    # manufacture = models.TextField(null=True, blank=True)
    # inc = models.ForeignKey('Income', blank=True, null=True, on_delete=models.PROTECT)

class Expense(models.Model):
    name = models.CharField(max_length=10)
    # intro = models.TextField(max_length=50)
    info = models.TextField()
    # img_link= models.TextField()
    # manufacture = models.TextField(null=True, blank=True)
    # exp = models.ForeignKey('Expense', blank=True, null=True, on_delete=models.PROTECT)
