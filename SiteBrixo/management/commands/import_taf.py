from django.core.management.base import BaseCommand
from ...models import Suppliers, Articles, ArticleOem, VehicleBrands, VehicleModels, Vehicles, ArticlesToVehicle, File, \
    DisplayBra
import os.path
import csv


def import_nibk():
    query = Articles.objects.filter(SupplierId__Name="NiBK").values('ArticleNumber', 'ExternalId')[:3]
    print(query)


class Command(BaseCommand):
    def handle(self, *args, **options):
        import_nibk()