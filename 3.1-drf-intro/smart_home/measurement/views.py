from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


# Создание датчика
class SensorCreateView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Изменение датчика
class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Получить список датчиков
class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Получить информацию по конкретному датчику
class SensorDetailView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

# Добавление измерения температуры
class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        sensor_id = self.request.data.get('sensor_id')
        sensor = Sensor.objects.get(id=sensor_id)
        serializer.save(sensor=sensor)