from django.db import models

# Create your models here.


class Income(models.Model):
    name = models.CharField(max_length=255)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    # Добавьте другие обязательные поля, если они есть

    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=10)
    # intro = models.TextField(max_length=50)
    info = models.TextField()
    # img_link= models.TextField()
    # manufacture = models.TextField(null=True, blank=True)
    # exp = models.ForeignKey('Expense', blank=True, null=True, on_delete=models.PROTECT)
