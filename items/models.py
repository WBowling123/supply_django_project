from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=180)
    type = models.CharField(max_length=120)  # TODO: ForeignKey
    category = models.CharField(max_length=120)  # TODO: ForeignKey
    size = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Item Parent Model"
        db_table = 'item_parent'
