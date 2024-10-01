from test_async import models# Reemplaza 'MyModel' con tu modelo real
from rest_framework.test import APIClient, APITestCase

class MyModelAPITestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(1000):
            models.MyModel.objects.create(
                name=f'Test Name {i}', 
                date='2024-01-01'  # Ajusta la fecha según sea necesario
            )

    def test_record_count(self):
        """Verifica si se crearon 1000 registros."""
        self.assertEqual(models.MyModel.objects.count(), 1000)

    def test_api_list_view(self):
        """Prueba la vista de listado de la API."""
        client = APIClient()
        response = client.get('/api/mymodel/')  # Reemplaza '/mymodels/' con la URL de tu API
        self.assertEqual(response.status_code, 200)  # Verifica que la solicitud fue exitosa
        self.assertEqual(len(response.data), 1000)  # Verifica que se obtuvieron 1000 registros
        
        
        response = client.post('/create_records/')  # Reemplaza '/mymodels/' con la URL de tu API
        response = client.post('/create_records_async/')  # Reemplaza '/mymodels/' con la URL de tu API
