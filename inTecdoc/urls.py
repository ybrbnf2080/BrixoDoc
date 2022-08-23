from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter(trailing_slash=False)
router.register(r'article', ArticleViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
