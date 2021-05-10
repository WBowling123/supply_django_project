from django.views import generic
from django.http import request, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MedicationSerializer
from .models import ItemMedication


class MedicationView(viewsets.ModelViewSet):
    serializer_class = MedicationSerializer
    queryset = ItemMedication.objects.all()


def index(request):
    all_medications = ItemMedication.objects.all()
    context = {
        'all_medications': all_medications
    }
    return render(request, 'medication/index.html', context)


def med_detail_view(request, med_id, *args, **kwargs):
    med = ItemMedication.objects.get(id=med_id)
    return HttpResponse(f"Generic Name: {med.name} / Brand Name: {med.brand_name}")


"""
class MedicationIndexView(generic.ListView):
    template_name = 'medication/index.html'
    context_object_name = 'medication_list'

    def get_queryset(self):
        return ItemMedication.objects.all()
"""
