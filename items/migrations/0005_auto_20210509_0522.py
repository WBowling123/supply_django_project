# Generated by Django 3.2.2 on 2021-05-09 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_itemtype_item_type_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name_plural': 'Item Categories'},
        ),
        migrations.RemoveField(
            model_name='itemasset',
            name='type',
        ),
        migrations.RemoveField(
            model_name='itemmedication',
            name='type',
        ),
    ]
