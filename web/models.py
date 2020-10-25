from django.db import models
from django.conf import settings
from django_currentuser.middleware import get_current_authenticated_user
from django.core.validators import RegexValidator
# Create your models here.


class BaseModel(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    last_updated_at = models.DateTimeField(auto_now=True, verbose_name="最終更新日時")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
        verbose_name="作成者", editable=False
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_last_updated_by",
        verbose_name="最終更新者", editable=False
    )
    is_active = models.BooleanField(default=True, verbose_name="有効")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_by = get_current_authenticated_user()
        self.last_updated_by = get_current_authenticated_user()
        super(BaseModel, self).save(*args, **kwargs)


class Area(BaseModel):
    name = models.CharField(max_length=10, verbose_name="都道府県名")
    region = models.CharField(max_length=10, verbose_name="地域")

    def __str__(self):
        return self.name


class ItemType(BaseModel):
    name = models.CharField(max_length=100, verbose_name="装置分類名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "装置分類"
        verbose_name_plural = "装置分類"


class Item(BaseModel):
    CHOICES_PRICE_TYPE = (
        ("〜1千万円", "〜1千万円"), ("1千万円~1億円", "1千万円~1億円"), ("1億円〜", "1億円〜")
    )
    CHOICES_STATUS = (
        ("作成中", "作成中"), ("承認待ち", "承認待ち"),
        ("承認済み", "承認済み"), ("商談中", "商談中"),
        ("成約済み", "成約済み"), ("取り下げ", "取り下げ"),
    )
    name = models.CharField(max_length=100, verbose_name="名前")
    item_type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING, verbose_name="装置分類")
    height = models.FloatField(verbose_name="高さ")
    width = models.FloatField(verbose_name="横幅")
    depth = models.FloatField(verbose_name="奥行")
    price_type = models.CharField(max_length=30, verbose_name="価格帯", choices=CHOICES_PRICE_TYPE)
    area = models.ForeignKey(Area, verbose_name="在庫都道府県", on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=20, verbose_name="ステータス", choices=CHOICES_STATUS, default="作成中")
    image01 = models.ImageField(verbose_name="画像01", blank=True, null=True, upload_to="images/")

    def __str__(self):
        return "Item{}_{}".format(self.pk, self.name)

    class Meta:
        verbose_name = "商品情報"
        verbose_name_plural = "商品情報"


class CaseType(BaseModel):
    name = models.CharField(max_length=100, verbose_name="問い合わせ分類")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "問い合わせ分類"
        verbose_name_plural = "問い合わせ分類"


class Case(BaseModel):
    tel_number_regex = RegexValidator(
        regex=r'^[0-9]+$', message=("携帯電話番号はハイフンなしで入力してください"),
    )
    # Fields
    objects = None
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="商品")
    memo = models.TextField(verbose_name="備考")
    assigned_at = models.DateTimeField(verbose_name="アサイン日時", blank=True, null=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="assigned_to",
        verbose_name="担当者", blank=True, null=True
    )
    case_type = models.ForeignKey(CaseType, on_delete=models.DO_NOTHING, verbose_name="問い合わせ分類")
    # 2020/10/25追加
    user_name = models.CharField(max_length=30, verbose_name="氏名", blank=True, null=True, )
    mail_address = models.EmailField(verbose_name="メールアドレス", blank=True, null=True, )
    company_name = models.CharField(
        max_length=100, verbose_name="会社名", blank=True, null=True, default=None,
    )
    company_address = models.CharField(
        max_length=100, verbose_name="会社住所", blank=True, null=True, default=None,
    )
    tel_number = models.CharField(
        validators=[tel_number_regex], max_length=15, verbose_name='携帯電話番号',
        blank=True, null=True, default=None,
    )

    def __str__(self):
        return "Case{}_{}".format(self.pk, self.item.name)

    class Meta:
        verbose_name = "問い合わせ"
        verbose_name_plural = "問い合わせ"
