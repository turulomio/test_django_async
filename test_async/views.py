from rest_framework import viewsets
from test_async import models, serializers

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = models.MyModel.objects.all()
    serializer_class = serializers.MyModelSerializer
