# Generated by Django 2.2.16 on 2020-09-29 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('last_updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('is_active', models.BooleanField(default=True, verbose_name='有効')),
                ('name', models.CharField(max_length=100, verbose_name='装置分類名')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_itemtype_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_itemtype_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('last_updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('is_active', models.BooleanField(default=True, verbose_name='有効')),
                ('name', models.CharField(max_length=100, verbose_name='名前')),
                ('height', models.FloatField(verbose_name='高さ')),
                ('width', models.FloatField(verbose_name='横幅')),
                ('depth', models.FloatField(verbose_name='奥行')),
                ('price_type', models.CharField(choices=[('〜1千万円', '〜1千万円'), ('1千万円~1億円', '1千万円~1億円'), ('1億円〜', '1億円〜')], max_length=30, verbose_name='価格帯')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_item_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.ItemType', verbose_name='装置分類')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_item_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('last_updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('is_active', models.BooleanField(default=True, verbose_name='有効')),
                ('name', models.CharField(max_length=100, verbose_name='問い合わせ分類')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_casetype_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_casetype_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('last_updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('is_active', models.BooleanField(default=True, verbose_name='有効')),
                ('memo', models.TextField(verbose_name='備考')),
                ('assigned_at', models.DateTimeField(blank=True, null=True, verbose_name='アサイン日時')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='担当者')),
                ('case_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web.CaseType', verbose_name='問い合わせ分類')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_case_created_by', to=settings.AUTH_USER_MODEL, verbose_name='作成者')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Item', verbose_name='商品')),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_case_last_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='最終更新者')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]