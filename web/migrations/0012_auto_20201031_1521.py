# Generated by Django 2.2.16 on 2020-10-31 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20201030_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_area_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='area',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_area_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者'),
        ),
        migrations.AlterField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_case_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='case',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_case_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者'),
        ),
        migrations.AlterField(
            model_name='casetype',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_casetype_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='casetype',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_casetype_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_item_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='item',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_item_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者'),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_itemtype_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者'),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='web_itemtype_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者'),
        ),
    ]
