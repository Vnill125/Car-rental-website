from rest_framework import serializers

from base.models import Vehicles


class VehiclesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = '__all__'
        
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    