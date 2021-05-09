import datetime

from django.db import models

from django.contrib.auth.models import User


class ItemCategory(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'item_category'

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(max_length=180)
    ITEM_TYPE_TAG_CHOICES = [
        ('M', 'MEDICATION'),
        ('S', 'SUPPLY')
    ]
    item_type_tag = models.CharField(choices=ITEM_TYPE_TAG_CHOICES, max_length=100)

    class Meta:
        db_table = 'item_type'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=180)
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    size = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Item Parent"
        db_table = 'item_parent'
        abstract = True


class Asset(Item):
    asset_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'item_asset'

    def __str__(self):
        return self.name
