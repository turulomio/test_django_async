from django.urls import path, include
from rest_framework import routers
from test_async import views 

router = routers.DefaultRouter()
router.register(r'mymodel/', views.MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
