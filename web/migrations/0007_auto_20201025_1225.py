# Generated by Django 2.2.16 on 2020-10-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201025_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='mail_address',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='メールアドレス'),
        ),
        migrations.AddField(
            model_name='case',
            name='user_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='氏名'),
        ),
    ]