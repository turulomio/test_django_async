from rest_framework import serializers
from test_async import models

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyModel
        fields = '__all__'  # Or specify the fields you want to include
