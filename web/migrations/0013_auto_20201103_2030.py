# Generated by Django 2.2.16 on 2020-11-03 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0012_auto_20201031_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='maker',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='メーカー'),
        ),
        migrations.AddField(
            model_name='item',
            name='model_detail',
            field=models.TextField(blank=True, null=True, verbose_name='仕様'),
        ),
        migrations.AddField(
            model_name='item',
            name='model_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='型式/型番'),
        ),
        migrations.AddField(
            model_name='item',
            name='model_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='年式'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='希望価格'),
        ),
        migrations.AddField(
            model_name='item',
            name='price_minimum',
            field=models.IntegerField(blank=True, help_text='画面には表示しない', null=True, verbose_name='下限価格'),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=255, verbose_name='都道府県名'),
        ),
        migrations.AlterField(
            model_name='area',
            name='region',
            field=models.CharField(max_length=255, verbose_name='地域'),
        ),
        migrations.AlterField(
            model_name='case',
            name='company_address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='会社住所'),
        ),
        migrations.AlterField(
            model_name='case',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='会社名'),
        ),
        migrations.AlterField(
            model_name='case',
            name='user_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='氏名'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='名前'),
        ),
        migrations.AlterField(
            model_name='item',
            name='price_type',
            field=models.CharField(blank=True, choices=[('〜1千万円', '〜1千万円'), ('1千万円~1億円', '1千万円~1億円'), ('1億円〜', '1億円〜')], max_length=255, null=True, verbose_name='価格帯'),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('作成中', '作成中'), ('承認待ち', '承認待ち'), ('承認済み', '承認済み'), ('商談中', '商談中'), ('成約済み', '成約済み'), ('取り下げ', '取り下げ')], default='作成中', max_length=255, verbose_name='ステータス'),
        ),
        migrations.AlterField(
            model_name='itemtype',
            name='name',
            field=models.CharField(max_length=255, verbose_name='装置分類名'),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Item', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ')),
            ],
        ),
    ]
