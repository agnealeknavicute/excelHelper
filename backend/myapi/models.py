# from django.db import models

# # Create your models here.


# class Income(models.Model):
#     name = models.CharField(max_length=255)
#     value = models.DecimalField(max_digits=10, decimal_places=2)
#     type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])

#     def __str__(self):
#         return f"{self.name} - {self.amount} ({self.type})"


# # models.py

# from django.db import models

# class Expense(models.Model):
#     # поля для модели Expense
#     title = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     # другие поля, которые вам нужны

from django.db import models

class Income(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])

    def __str__(self):
        return f"{self.name} - {self.value} ({self.type})"

from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('expense', 'Expense')])

    def __str__(self):
        return f"{self.name} - {self.amount} ({self.type})"

