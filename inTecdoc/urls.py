from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from rest_framework import routers

from . import views
from .views import *


router = routers.SimpleRouter()
# router.register(r'article', APIView)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    path("api/v1/article/", views.ArticleAPIView.as_view()),
    path("api/v1/article/<int:pk>/", views.ArticleAPIViewItem.as_view()),
]
