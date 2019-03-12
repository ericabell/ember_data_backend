from rest_framework import serializers
from v1_backend.models import Rental

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ('id', 'title', 'owner', 'city', 'category', 'image', 'bedrooms', 'description')
