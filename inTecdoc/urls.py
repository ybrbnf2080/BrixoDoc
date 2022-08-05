from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter(trailing_slash=False)
router.register(r'table203', Table203ViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
