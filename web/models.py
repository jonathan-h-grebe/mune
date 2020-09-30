from django.db import models
from django.conf import settings
# Create your models here.


class BaseModel(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    last_updated_at = models.DateTimeField(auto_now=True, verbose_name="最終更新日時")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_created_by",
        verbose_name="作成者",
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_last_updated_by",
        verbose_name="最終更新者"
    )
    is_active = models.BooleanField(default=True, verbose_name="有効")

    class Meta:
        abstract = True


class Area(BaseModel):
    name = models.CharField(max_length=10, verbose_name="都道府県名")
    region = models.CharField(max_length=10, verbose_name="地域")

    def __str__(self):
        return self.name


class ItemType(BaseModel):
    name = models.CharField(max_length=100, verbose_name="装置分類名")

    def __str__(self):
        return self.name


class Item(BaseModel):
    CHOICES_PRICE_TYPE = (
        ("〜1千万円", "〜1千万円"), ("1千万円~1億円", "1千万円~1億円"),
        ("1億円〜", "1億円〜")
    )
    name = models.CharField(max_length=100, verbose_name="名前")
    item_type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING, verbose_name="装置分類")
    height = models.FloatField(verbose_name="高さ")
    width = models.FloatField(verbose_name="横幅")
    depth = models.FloatField(verbose_name="奥行")
    price_type = models.CharField(max_length=30, verbose_name="価格帯", choices=CHOICES_PRICE_TYPE)
    area = models.ForeignKey(Area, verbose_name="在庫都道府県", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "Item{}_{}".format(self.pk, self.name)


class CaseType(BaseModel):
    name = models.CharField(max_length=100, verbose_name="問い合わせ分類")

    def __str__(self):
        return self.name


class Case(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="商品")
    memo = models.TextField(verbose_name="備考")
    assigned_at = models.DateTimeField(verbose_name="アサイン日時", blank=True, null=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="assigned_to",
        verbose_name="担当者", blank=True, null=True
    )
    case_type = models.ForeignKey(CaseType, on_delete=models.DO_NOTHING, verbose_name="問い合わせ分類")

    def __str__(self):
        return "Case{}_{}".format(self.pk, self.item.name)

