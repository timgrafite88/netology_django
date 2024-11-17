from django.urls import path
from .views import (
    SensorCreateView,
    SensorUpdateView,
    SensorListView,
    SensorDetailView,
    MeasurementCreateView,
)

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('sensors/create/', SensorCreateView.as_view(), name='sensor-create'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensors/<int:pk>/update/', SensorUpdateView.as_view(), name='sensor-update'),
    path('measurements/create/', MeasurementCreateView.as_view(), name='measurement-create'),
]
