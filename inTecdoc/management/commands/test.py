import os.path
from django.conf import settings
from django.core.management.base import BaseCommand
import pandas as pd

from datetime import datetime

from inTecdoc.models import *

BASE_DIR = settings.BASE_DIR


def get_suppliers():
    start_time = datetime.now()
    path = os.path.join(BASE_DIR, 'ImportTAF/suppliers.txt')
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            try:
                _, created = Suppliers200.objects.get_or_create(
                    brand_no=line[0:5],
                    name=line[5:]
                )
            except:
                print('Error')
    print("Время работы скрипта", datetime.now() - start_time)


def get_country():
    path = os.path.join(BASE_DIR, 'ImportTAF/country.txt')
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            try:
                _, created = Country202.objects.get_or_create(
                    country_code=line[0:4],
                    country_name=line[4:]
                )
            except:
                print('Error')
    print('------add Country--------')


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


def get_criteria_pd():
    tmp_data = pd.read_csv(os.path.join(BASE_DIR, 'ImportTAF/criteria.csv'), sep=';')
    criteria = [
        CritVal210(
            crit_no=tmp_data.loc[row][0],
            name=tmp_data.loc[row][1],
        )
        for row in tmp_data.index
    ]
    CritVal210.objects.bulk_create(criteria)
    print('------add criteria--------')


def get_ref():
    start_time = datetime.now()
    path = os.path.join(BASE_DIR, 'ImportTAF/203.4682')
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            try:
                _, created = Ref203.objects.get_or_create(
                    man_no_id=Manufacture203.objects.filter(man_no=line[29:35]).first(),
                    ref_no=line[38:60]
                )
            except:
                print('Error')
    print("Время работы скрипта", datetime.now() - start_time)


def get_supers():
    start_time = datetime.now()
    path = os.path.join(BASE_DIR, 'ImportTAF/204.4682')
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            try:
                _, created = Supers204.objects.get_or_create(
                    supers_no=line[32:54]
                )
            except:
                print('Error')
    print("Время работы скрипта", datetime.now() - start_time)


def get_doc():
    start_time = datetime.now()
    path = os.path.join(BASE_DIR, 'ImportTAF/231.4682')
    with open(path, "r", encoding='utf-8') as f:
        i = 1
        for line in f:
            # if i < 5:
            #     print(line[41:71])
            #     i += 1
            try:
                _, created = Doc231and232.objects.get_or_create(
                    doc_no=int(line[29:38]),
                    lang_no=int(line[38:41]),
                    doc_name=line[41:71],
                    doc_type=int(line[71:74]),
                    doc_type_one=int(line[88:90])
                )
            except:
                print('Error')
    print("Время работы скрипта", datetime.now() - start_time)


def clear_data():
    """
    Очистить все записи в БД
    """
    Suppliers200.objects.all().delete()
    Country202.objects.all().delete()
    Manufacture203.objects.all().delete()
    CritVal210.objects.all().delete()
    Ref203.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # get_manufacturer_pd()
        # clear_data()
        # get_suppliers()
        # get_country()
        # get_manufacturer_pd()
        # get_criteria_pd()
        # get_ref()
        # get_supers()
        # get_doc()
        # test()
        # get_article()
        pass

