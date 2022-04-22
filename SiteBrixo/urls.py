from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('suppliers/', views.SuppliersList.as_view()),
    path('suppliers/<int:pk>/', views.SuppliersDetail.as_view()),
    path('article/', views.ArticlesList.as_view()),
    path('article/<int:pk>/', views.ArticlesDetail.as_view()),
    path('articleoem/', views.ArticlesOemList.as_view()),
    path('articleoem/<int:pk>/', views.ArticlesOemDetail.as_view()),
    path('vehiclebrand/', views.VehicleBrandList.as_view()),
    path('vehiclebrand/<int:pk>/', views.VehicleBrandDetail.as_view()),
    path('vehiclemodel/', views.VehicleModelList.as_view()),
    path('vehiclemodel/<int:pk>/', views.VehicleModelDetail.as_view()),
    path('vehicles/', views.VehicleList.as_view()),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view()),
    path('displaybra/', views.DisplayBraList.as_view()),
    path('displaybra/<int:pk>/', views.DisplayBraDetail.as_view()),

]