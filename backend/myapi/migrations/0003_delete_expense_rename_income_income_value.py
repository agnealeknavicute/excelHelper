# Generated by Django 5.0.1 on 2024-01-16 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_value_income_income'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='income',
            new_name='value',
        ),
    ]