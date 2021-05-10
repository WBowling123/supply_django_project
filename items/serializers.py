from rest_framework import serializers
from .models import ItemMedication


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMedication
        fields = ('id', 'name', 'brand_name', 'is_controlled')
