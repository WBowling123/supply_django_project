from django.views import generic
from django.http import request
from django.shortcuts import render

from .models import ItemMedication


def index(request):
    all_medications = ItemMedication.objects.all()
    context = {
        'all_medications': all_medications
    }
    return render(request, 'medication/index.html', context)


"""
class MedicationIndexView(generic.ListView):
    template_name = 'medication/index.html'
    context_object_name = 'medication_list'

    def get_queryset(self):
        return ItemMedication.objects.all()
"""
