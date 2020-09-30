from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.


class CustomUser(AbstractUser): 
    """ 拡 張 ユーザーモデル""" 
    class Meta(AbstractUser.Meta): 
        db_table = 'custom_user' 

    age = models.IntegerField('年齢', blank=True, null=True)
    company_name = models.CharField(
        max_length=100, verbose_name="会社名",
        blank=True, null=True, default=None,
    )
    company_address = models.CharField(
        max_length=100, verbose_name="会社住所",
        blank=True, null=True, default=None,
    )
    # https://qiita.com/xKxAxKx/items/86bdf0bc4c7dc9ee65d9
    tel_number_regex = RegexValidator(
        regex=r'^[0-9]+$', message=("携帯電話番号はハイフンなしで入力してください"),
    )
    tel_number = models.CharField(
        validators=[tel_number_regex], max_length=15, verbose_name='携帯電話番号',
        blank=True, null=True, default=None,
    )
