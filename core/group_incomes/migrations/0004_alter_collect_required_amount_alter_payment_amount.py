# Generated by Django 4.2.11 on 2024-03-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("group_incomes", "0003_alter_payment_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collect",
            name="required_amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=15, verbose_name="Необходимая сумма"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=9, verbose_name="Сумма доната"
            ),
        ),
    ]