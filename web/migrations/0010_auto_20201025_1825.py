# Generated by Django 2.2.16 on 2020-10-25 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20201025_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='company_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='会社住所'),
        ),
        migrations.AlterField(
            model_name='case',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='会社名'),
        ),
        migrations.AlterField(
            model_name='case',
            name='tel_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='携帯電話番号はハイフンなしで入力してください', regex='^[0-9]+$')], verbose_name='携帯電話番号'),
        ),
    ]
