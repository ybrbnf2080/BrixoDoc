from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Suppliers, Articles, ArticleOem, VehicleBrands, VehicleModels, Vehicles, DisplayBra


class DisplayBraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayBra
        fields = [
            'id',
            'bra_brand_no',
            'bra_short_name',
            'view_term_plain',
        ]


class SuppliersSerializer(serializers.ModelSerializer):
    # suppliers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Suppliers
        fields = ['id', 'Name']


class ArticlesSerializer(serializers.ModelSerializer):
    SupplierId = serializers.ReadOnlyField(source='SupplierId.Name')

    class Meta:
        model = Articles
        fields = [
            'id',
            'ExternalId',
            'SupplierId',
            'AssemblyGroup',
            'GenericArticle',
            'ArticleNumber',
            'Type',
            'GenericArticleNumber',
            'Attributes',
        ]


class ArticleOemSerializer(serializers.ModelSerializer):
    ArticleId = serializers.ReadOnlyField(source='ArticleId.ArticleNumber')

    class Meta:
        model = ArticleOem
        fields = [
            'id',
            'Brand',
            'OemNumber',
            'ArticleId',
            'IsOriginal',
            'NormalizerOemNumber',
            'IsReplacer',
        ]


# class VehicleBrandSerializer(serializers.ModelSerializer):
#     Name = VehicleModelSerializer(many=True)
#
#
#     class Meta:
#         model = VehicleBrands
#         fields = [
#             'id',
#             'Name',
#         ]
class VehicleSerializer(serializers.ModelSerializer):
    VehicleModelId = serializers.ReadOnlyField(source='VehicleModelId.Name')

    class Meta:
        model = Vehicles
        fields = "__all__"


class VehicleModelSerializer(serializers.ModelSerializer):
    Vehicles = serializers.StringRelatedField(many=True)

    class Meta:
        model = VehicleModels
        fields = [
            'VehicleBrandId',
            'Name',
            'ModelNumber',
            'Vehicles',
        ]


class VehicleBrandSerializer(serializers.ModelSerializer):
    VehicleModels = VehicleModelSerializer(many=True)

    class Meta:
        model = VehicleBrands
        fields = [
            'id',
            'Name',
            'VehicleModels',
        ]
