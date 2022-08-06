import os.path
from shutil import rmtree
import csv

from django.db.models import *
from django.conf import settings
from django.core.management.base import BaseCommand
import pandas as pd

from datetime import datetime
import time

from inTecdoc.models import (Suppliers200, Article200, Lnk400, Country202, Manufacture203)

BASE_DIR = settings.BASE_DIR


def get_country():
    path = os.path.join(BASE_DIR, 'ImportTAF/country.txt')
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            try:
                _, created = Country202.objects.get_or_create(
                    country_code=line[0:4],
                    country_name=line[5:]
                )
            except:
                print('Error')
    print('------add Country--------')


def get_country_pd():
    start_time = datetime.now()
    tmp_data = pd.read_csv(os.path.join(BASE_DIR, 'ImportTAF/country.txt'), sep=';')
    country = [
        Country202(
            country_code=tmp_data.loc[row],
            country_name=tmp_data.loc[row]
        )
        for row in tmp_data.index
    ]
    print(tmp_data.loc)
    # Country202.objects.bulk_create(country)
    print('------add Country--------')
    print("Время работы скрипта", datetime.now() - start_time)


def get_manufacturer():
    start_time = datetime.now()
    path = os.path.join(BASE_DIR, 'ImportTAF/manufacturer.csv')
    with open(path, "r", encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        print()
        for row in reader:
            try:
                _, created = Manufacture203.objects.get_or_create(
                    man_no=int(row[0]),
                    short_name=row[1],
                    term_plain=row[2]
                )
            except:
                print("Error")
    print("Время работы скрипта", datetime.now() - start_time)

    print('------add Manufacturer--------')


def get_manufacturer_pd():
    start_time = datetime.now()
    tmp_data = pd.read_csv(os.path.join(BASE_DIR, 'ImportTAF/manufacturer.csv'), sep=';')
    manufacturer = [
        Manufacture203(
            man_no=tmp_data.loc[row][0],
            short_name=tmp_data.loc[row][1],
            term_plain=tmp_data.loc[row][2]
        )
        for row in tmp_data.index
    ]
    Manufacture203.objects.bulk_create(manufacturer, batch_size=500)
    print('------add Manufacturer--------')
    print("Время работы скрипта", datetime.now() - start_time)


def clear_data():
    """
    Очистить все записи в БД
    """
    Manufacture203.objects.all().delete()
    Country202.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_country_pd()
        # get_manufacturer_pd()
        # get_country()
        # clear_data()
        # get_manufacturer()
