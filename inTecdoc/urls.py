from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'article', ArticleViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
