from rest_framework import generics

from api.serializer import VehiclesModelSerializer
from api.mixins import IsStaffEditorMixin
from base.models import Vehicles

# Create your views here.

class VehicleApiView(
    generics.ListCreateAPIView,
    IsStaffEditorMixin
    ):
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesModelSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        results = qs.is_available()
        return results
