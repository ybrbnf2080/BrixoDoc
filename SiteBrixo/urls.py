from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from .views import BrandModelList


router = SimpleRouter(trailing_slash=False)


router.register('filter', BrandModelList, basename='name')

urlpatterns = [
    path('suppliers/', views.SuppliersList.as_view()),   #производитель
    path('suppliers/<int:pk>/', views.SuppliersDetail.as_view()),
    path('article/', views.ArticlesList.as_view()),  #Все артикулы
    path('article/<int:pk>/', views.ArticlesDetail.as_view()),
    path('articleoem/', views.ArticlesOemList.as_view()),  #Оем Артикулы
    path('articleoem/<int:pk>/', views.ArticlesOemDetail.as_view()),
    path('vehiclebrand/', views.VehicleBrandList.as_view()),  #Бренды Авто
    path('vehiclebrand/<int:pk>/', views.VehicleBrandDetail.as_view()),
    path('vehiclemodel/', views.VehicleModelList.as_view()),  #Марки автоz
    path('vehiclemodel/<int:pk>/', views.VehicleModelDetail.as_view()),
    path('vehicles/', views.VehicleList.as_view()),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view()),
    path('displaybra/', views.DisplayBraList.as_view()),
    path('displaybra/<int:pk>/', views.DisplayBraDetail.as_view()),
    path('fit/', views.FitList.as_view()),
    path('brixo/', views.BrixoList.as_view()),
    path('sure/', views.SureList.as_view()),
    path('nibk/', views.NiBKList.as_view()),
    path('js/', views.JSList.as_view()),
    path('sacura/', views.SacuraList.as_view()),
]

urlpatterns += router.urls