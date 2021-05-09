import datetime

from django.db import models

from django.contrib.auth.models import User


class ItemCategory(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        db_table = 'item_category'
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return self.name


class ItemType(models.Model):
    name = models.CharField(max_length=180)

    class Meta:
        db_table = 'item_type'

    def __str__(self):
        return self.name


# TODO(!!): figure out User model integration.
class Item(models.Model):
    """
    Parent class for below item models
    """
    name = models.CharField(max_length=180)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    size = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Item Parent"
        db_table = 'item_parent'
        abstract = True


class ItemAsset(Item):
    asset_id = models.CharField(max_length=20)

    class Meta:
        db_table = 'item_asset'

    def __str__(self):
        return self.name


class ItemMedication(Item):
    brand_name = models.CharField(max_length=120)
    concentration = models.CharField(max_length=40)
    is_controlled = models.BooleanField(default=False)

    class Meta:
        db_table = 'item_medication'

    def __str__(self):
        return '%s (%s)' % (
            self.name,
            self.brand_name
        )
