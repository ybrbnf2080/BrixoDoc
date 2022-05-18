from rest_framework import generics, viewsets
from . import serializers
from .models import Suppliers, Articles, ArticleOem, VehicleBrands, VehicleModels, Vehicles, DisplayBra


class DisplayBraList(generics.ListAPIView):
    queryset = DisplayBra.objects.all()
    serializer_class = serializers.DisplayBraSerializer


class DisplayBraDetail(generics.RetrieveAPIView):
    queryset = DisplayBra.objects.all()
    serializer_class = serializers.DisplayBraSerializer


class SuppliersList(generics.ListAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = serializers.SuppliersSerializer


class SuppliersDetail(generics.RetrieveAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = serializers.SuppliersSerializer


class ArticlesList(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticlesSerializer


class ArticlesDetail(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticlesSerializer


class ArticlesOemList(generics.ListAPIView):
    queryset = ArticleOem.objects.all()
    serializer_class = serializers.ArticleOemSerializer


class ArticlesOemDetail(generics.RetrieveAPIView):
    queryset = ArticleOem.objects.all()
    serializer_class = serializers.ArticleOemSerializer


class VehicleBrandList(generics.ListAPIView):
    queryset = VehicleBrands.objects.all()
    serializer_class = serializers.VehicleBrandSerializer


class VehicleBrandDetail(generics.RetrieveAPIView):
    queryset = VehicleBrands.objects.all()
    serializer_class = serializers.VehicleBrandSerializer


class VehicleModelList(generics.ListAPIView):
    queryset = VehicleModels.objects.all()
    serializer_class = serializers.VehicleModelSerializer


class BrandModelList(viewsets.ModelViewSet):
    queryset = VehicleBrands.objects.all()
    serializer_class = serializers.VehicleBrandSerializer

class VehicleModelDetail(generics.RetrieveAPIView):
    queryset = VehicleModels.objects.all()
    serializer_class = serializers.VehicleModelSerializer


class VehicleList(generics.ListAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = serializers.VehicleSerializer


class VehicleDetail(generics.RetrieveAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = serializers.VehicleSerializer