from django.views import generic
from django.http import request
from django.shortcuts import render

from .models import ItemCategory, Item, ItemMedication, ItemType, ItemAsset


class MedicationIndexView(generic.ListView):
    template_name = 'medications/index.html'
    context_object_name = 'medication_list'

    def get_queryset(self):
        return ItemMedication.objects.all()

