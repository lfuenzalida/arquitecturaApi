from django.urls import path, include
from rest_framework import routers
from finalBoss import views

router = routers.DefaultRouter()
router.register(r'raw-data', views.RawDataViewSet)
router.register(r'transformed-data', views.TransformedDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
