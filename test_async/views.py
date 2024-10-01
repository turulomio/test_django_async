from rest_framework import viewsets
from test_async import models, serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from time import monotonic
from functools import wraps


def execution_time_api_view(view_method):
    """Decorador para medir y mostrar el tiempo de ejecución de un método de APIView."""

    @wraps(view_method)
    def wrapper(self, request, *args, **kwargs):
        start_time = monotonic()
        response = view_method(self, request, *args, **kwargs)
        end_time = monotonic()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"Tiempo de ejecución de {self.__class__.__name__}.{view_method.__name__}: {execution_time_ms:.2f} ms")
        return response

    return wrapper

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = models.MyModel.objects.all()
    serializer_class = serializers.MyModelSerializer

class CreateRecordsView(APIView):
    
    @execution_time_api_view
    def post(self, request):
        """Crea 1000 registros de forma síncrona."""

        for i in range(1000):
            models.MyModel.objects.create(
                name=f'Test Name {i}',
                date='2024-01-01' 
            )

        return Response(status=status.HTTP_201_CREATED)

class CreateRecordsViewAsync(APIView):
    
    @execution_time_api_view
    async def post(self, request):
        """Crea 1000 registros de forma asíncrona."""
        

        async def create_records_task():
            for i in range(1000):
                await models.MyModelMyModel.objects.acreate(
                    name=f'Test Name {i}',
                    date='2024-01-01'
                )
            
        await create_records_task()
        return Response(status=status.HTTP_201_CREATED)
