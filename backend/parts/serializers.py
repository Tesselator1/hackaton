from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Part

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'name')

