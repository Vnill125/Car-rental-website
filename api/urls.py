from django.urls import path

from . import views

urlpatterns = [
    path('vehicles/', views.VehicleApiView.as_view(), name='vehicle_api')
]
