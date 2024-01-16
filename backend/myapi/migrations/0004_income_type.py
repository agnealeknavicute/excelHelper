# Generated by Django 5.0.1 on 2024-01-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_delete_expense_rename_income_income_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='type',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], default='unknown', max_length=10),
            preserve_default=False,
        ),
    ]
