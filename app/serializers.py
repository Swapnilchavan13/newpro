from rest_framework import serializers
from .models import *




class ImageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

        