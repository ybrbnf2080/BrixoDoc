from django.core.management.base import BaseCommand
from ...models import Suppliers, Articles, ArticleOem, VehicleBrands
import os.path
import csv

BASE_DIR = 'C:/Users/Sirius_McLine/Desktop/Brixo Doc/BrixoDoc/'


def get_article():
    path = os.path.join(BASE_DIR, 'ImportCSV/articles.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            _, created = Articles.objects.get_or_create(
                ExternalId=row[0],
                SupplierId=Suppliers.objects.get(Name=row[3]),
                AssemblyGroup=row[4],
                GenericArticle=row[5],
                ArticleNumber=row[1],
                Type=1,
                GenericArticleNumber=row[2],
                Attributes=row[6],
            )


def get_oem():
    path = os.path.join(BASE_DIR, 'ImportCSV/articles_oem.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            _, created = ArticleOem.objects.get_or_create(
                Brand=row[1],
                OemNumber=row[3].upper(),
                ArticleId=Articles.objects.get(ExternalId=row[0]),
                IsOriginal=row[2],
                NormalizerOemNumber=row[3].lower(),
                IsReplacer=row[4],
            )


def get_vehicle_brand():
    path = os.path.join(BASE_DIR, 'ImportCSV/vehicles.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            _, created = VehicleBrands.objects.get_or_create(
                Name=row[2]
            )


def clear_data():
    """
    Очистить все записи в таблице
    """
    # Articles.objects.all().delete()
    ArticleOem.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        # get_article()
        get_oem()