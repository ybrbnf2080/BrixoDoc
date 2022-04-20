from django.core.management.base import BaseCommand
from django.conf import settings
from ...models import Suppliers, Articles
import os.path
import csv
import pandas as pd


def create_product():
    tmp_data = pd.read_csv('C:/Users/Sirius_McLine/PycharmProjects/BrixoDoc/ImportCSV/articles.csv', sep=';')
    product_db = Articles(
        ExternalId=tmp_data[0],
        SupplierId=Suppliers.objects.get(id=tmp_data[3]),
        AssemblyGroup=tmp_data[4],
        GenericArticle=tmp_data[5],
        ArticleNumber=tmp_data[1],
        Type=1,
        GenericArticleNumber=8,
    )
    product_db.save()


def clear_data():
    """
    Очистить все записи в таблице Product
    """
    Articles.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_data()
        create_product()
