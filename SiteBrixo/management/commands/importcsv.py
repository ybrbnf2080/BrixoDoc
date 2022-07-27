from django.core.management.base import BaseCommand
from ...models import Suppliers, Articles, ArticleOem, VehicleBrands, VehicleModels, Vehicles, ArticlesToVehicle, File, \
    DisplayBra
import os.path
import csv

BASE_DIR = 'C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc'


def get_article():
    path = os.path.join(BASE_DIR, 'ImportCSV/articles.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
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
            except:
                print('reader Articles', reader)
                print('created Articles', created)
    print('------add ARTICLE--------')


def get_oem():
    path = os.path.join(BASE_DIR, 'ImportCSV/articles_oem.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = ArticleOem.objects.get_or_create(
                    Brand=row[1],
                    OemNumber=row[3].upper(),
                    ArticleId=Articles.objects.get(ExternalId=row[0]),
                    IsOriginal=row[2],
                    NormalizerOemNumber=row[3].lower(),
                    IsReplacer=row[4],
                )
            except:
                print('reader ArticleOem', reader)
                print('created ArticleOem', created)
    print('------add OEM--------')


def get_vehicle_brand():
    path = os.path.join(BASE_DIR, 'ImportCSV/vehicles.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = VehicleBrands.objects.get_or_create(
                    Name=row[2]
                )
            except:
                print('reader VehicleBrands', reader)
                print('created VehicleBrands', created)
    print('------add VEHICLE BRAND--------')


def get_vehicle_model():
    path = os.path.join(BASE_DIR, 'ImportCSV/vehicles.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = VehicleModels.objects.get_or_create(
                    VehicleBrandId=VehicleBrands.objects.filter(Name=row[2]).first(),
                    Name=row[3],
                    ModelNumber=row[1]
                )
            except:
                print('reader VehicleModels', reader)
                print('created VehicleModels', created)
    print('------add VEHICLE MODEL--------')


def get_vehicle():
    path = os.path.join(BASE_DIR, 'ImportCSV/vehicles.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = Vehicles.objects.get_or_create(
                    VehicleModelId=VehicleModels.objects.filter(Name=row[3]).first(),
                    TypeNumber=row[0],
                    Year=row[6],
                    BodyType=row[7],
                    DriveType=row[8],
                    EngineType=row[9],
                    ValvesPerChamber=row[10],
                    Cylinders=row[11],
                    Volume=row[12],
                    CcmTech=row[13],
                    FuelType=row[14],
                    FuelMixtureFormation=row[15],
                    HorsePowers=row[16],
                    KiloWatts=row[17],
                    Engines=row[5],
                    TypeName=row[4],
                )
            except:
                print('reader Vehicles', reader)
                print('created Vehicles', created)
    print('------add VEHICLE--------')


def get_articles_to_vehicle():
    path = os.path.join(BASE_DIR, 'ImportCSV/article_vehicle_links.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = ArticlesToVehicle.objects.get_or_create(
                    ArticleId=Articles.objects.filter(ExternalId=row[0]).first(),
                    VehicleId=Vehicles.objects.filter(TypeNumber=row[1]).first(),
                    Criterias=row[3],
                    ExternalId=row[0],
                )
            except:
                print('reader ArticlesToVehicle', reader)
                print('created ArticlesToVehicle', created)
    print('------add ARTICLE_TO_VEHICLE--------')


def get_file():
    path = os.path.join(BASE_DIR, 'ImportCSV/article_files.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = File.objects.get_or_create(
                    ArticleId=Articles.objects.filter(ExternalId=row[0]).first(),
                    Path=row[1],
                    Order=row[2],
                )
            except:
                print('reader File', reader)
                print('created File', created)
    print('------add FILE PATH--------')


def get_display_bra():
    path = os.path.join(BASE_DIR, 'ImportCSV/article_files.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)
        for row in reader:
            try:
                _, created = DisplayBra.objects.get_or_create(
                    bra_brand_no=row[0],
                    bra_short_name=row[1],
                    view_term_plain=row[2],
                )
            except:
                print('reader DisplayBra', reader)
                print('created DisplayBra', created)
    print('------add DisplayBra--------')


def clear_data():
    """
    Очистить все записи в БД
    """
    Articles.objects.all().delete()
    ArticleOem.objects.all().delete()
    VehicleBrands.objects.all().delete()
    VehicleModels.objects.all().delete()
    Vehicles.objects.all().delete()
    ArticlesToVehicle.objects.all().delete()
    File.objects.all().delete()
    DisplayBra.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
        # clear_data()
        # get_article()
        # get_oem()
        # get_vehicle_brand()
        # get_vehicle_model()
        # get_vehicle()
        # get_articles_to_vehicle()
        # get_file()
        # get_display_bra()
