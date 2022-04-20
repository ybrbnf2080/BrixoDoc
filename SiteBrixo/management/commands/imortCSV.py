from django.core.management.base import BaseCommand
import pandas as pd
from ...models import Suppliers, Articles, ArticleOem, VehicleBrands, VehicleModels, Vehicles, ArticlesToVehicle, File


def get_articles():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/articles.csv', sep=';')
    articles = [
        Articles(
            ExternalId=tmp_data.loc[row]['ART_ID'],
            SupplierId=Suppliers.objects.get(Name=tmp_data.loc[row]['SUP_NAME']),
            AssemblyGroup=tmp_data.loc[row]['Assembly_Group'],
            GenericArticle=tmp_data.loc[row]['Generic_Article'],
            ArticleNumber=tmp_data.loc[row]['ART_NUM'],
            Type=1,
            GenericArticleNumber=tmp_data.loc[row]['GEN_ART_NO'],
            Attributes=tmp_data.loc[row]['ATTRIBUTES'],
        )
        for row in tmp_data.index
    ]
    Articles.objects.bulk_create(articles)
    print('------add ARTICLE--------')


def get_oem():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/articles_oem.csv', sep=';')
    oem = [
        ArticleOem(
            Brand=tmp_data.loc[row]['OEM_BRAND'],
            OemNumber=tmp_data.loc[row]['OEM_NUM'],
            ArticleId=Articles.objects.get(ExternalId=tmp_data.loc[row]['ART_ID']),
            IsOriginal=tmp_data.loc[row]['OEM_COMPETITOR'],
            NormalizerOemNumber=tmp_data.loc[row]['OEM_NUM'],
            IsReplacer=tmp_data.loc[row]['REPLACE'],
        )
        for row in tmp_data.index
    ]
    ArticleOem.objects.bulk_create(oem)
    print('------add OEM--------')


def get_vehicle_brand():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/vehicles.csv',
                           sep=';').drop_duplicates(["VEH_BRAND"])
    vehicle_brand = [
        VehicleBrands(
            Name=tmp_data.loc[row]['VEH_BRAND']
        )
        for row in tmp_data.index
    ]
    VehicleBrands.objects.bulk_create(vehicle_brand)
    print('------add VEHICLE BRAND--------')
    print(tmp_data)


def get_vehicle_model():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/vehicles.csv',
                           sep=';').drop_duplicates(["VEH_MODEL_INTL"])
    vehicle_model = [
        VehicleModels(
            VehicleBrandId=VehicleBrands.objects.filter(Name=tmp_data.loc[row]['VEH_BRAND']).first(),
            Name=tmp_data.loc[row]['VEH_MODEL_INTL'],
            ModelNumber=tmp_data.loc[row]['VEH_MODEL_NO'],
        )
        for row in tmp_data.index
    ]
    VehicleModels.objects.bulk_create(vehicle_model)
    print('------add VEHICLE MODEL--------')


def get_vehicle():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/vehicles.csv', sep=';')
    vehicle = [
        Vehicles(
            VehicleModelId=VehicleModels.objects.filter(Name=tmp_data.loc[row]['VEH_MODEL_INTL']).first(),
            TypeNumber=tmp_data.loc[row]['VEH_TYPE_NO'],
            Year=tmp_data.loc[row]['YEAR'],
            BodyType=tmp_data.loc[row]['BODY_TYPE'],
            DriveType=tmp_data.loc[row]['DRIVE_TYPE'],
            EngineType=tmp_data.loc[row]['ENGINE_TYPE'],
            ValvesPerChamber=tmp_data.loc[row]['VALVES_PER_CHAMBER'],
            Cylinders=tmp_data.loc[row]['CYLINDERS'],
            Volume=tmp_data.loc[row]['LITRES'],
            CcmTech=tmp_data.loc[row]['CCM_TECH'],
            FuelType=tmp_data.loc[row]['FUEL_TYPE'],
            FuelMixtureFormation=tmp_data.loc[row]['FUEL_MIXTURE_FORMATION'],
            HorsePowers=tmp_data.loc[row]['HP'],
            KiloWatts=tmp_data.loc[row]['KW'],
            Engines=tmp_data.loc[row]['ENGINE_CODE'],
            TypeName=tmp_data.loc[row]['VEH_TYPE_NAME'],
        )
        for row in tmp_data.index
    ]
    Vehicles.objects.bulk_create(vehicle)
    print('------add VEHICLE--------')


def get_articles_to_vehicle():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/article_vehicle_links.csv',
                           sep=';')
    articles_to_vehicle = [
        ArticlesToVehicle(
            ArticleId=Articles.objects.filter(ExternalId=tmp_data.loc[row]['ART_ID']).first(),
            VehicleId=Vehicles.objects.filter(TypeNumber=tmp_data.loc[row]['VEH_TYPE_NO']).first(),
            Criterias=tmp_data.loc[row]['CRITERIAS'],
            ExternalId=tmp_data.loc[row]['ART_ID'],
        )
        for row in tmp_data.index
    ]
    ArticlesToVehicle.objects.bulk_create(articles_to_vehicle)
    print('------add ARTICLE_TO_VEHICLE--------')


def get_file():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/article_files.csv',
                           sep=';')
    files = [
        File(
            #VehicleId=Vehicles.objects.filter(TypeNumber=tmp_data.loc[row]['ART_ID']).first(),
            ArticleId=Articles.objects.filter(ExternalId=tmp_data.loc[row]['ART_ID']).first(),
            Path=tmp_data.loc[row]['FILE_NAME'],
            Order=tmp_data.loc[row]['FILE_ORDER'],
        )
        for row in tmp_data.index
    ]
    File.objects.bulk_create(files)
    print('------add FILE PATH--------')


def clear_data():
    Articles.objects.all().delete()
    ArticleOem.objects.all().delete()
    VehicleBrands.objects.all().delete()
    VehicleModels.objects.all().delete()
    Vehicles.objects.all().delete()
    ArticlesToVehicle.objects.all().delete()


def start():
    pass
    # get_articles()
    # get_oem()
    # get_vehicle_brand()
    # get_vehicle_model()
    # get_vehicle()
    # get_articles_to_vehicle()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # clear_data()
        # get_articles()
        # get_oem()
        # get_vehicle_brand()
        # get_vehicle_model()
        # get_vehicle()
        # get_articles_to_vehicle()
        get_file()


        print("-------------CSV IN DB WAS ADDED-------------")
