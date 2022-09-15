import os
from django.conf import settings
from django.core.management.base import BaseCommand
import time
import pandas as pd
from inTecdoc.models import *

pd.options.mode.chained_assignment = None
BASE_DIR = settings.BASE_DIR


def get_image():
    dirname = f'{BASE_DIR}/ImportTAF/sources_tec/image/'
    files = os.listdir(dirname)
    i = 0
    for image_name in files:
        image = image_name[:image_name.find('.')]
        image_query = Doc231and232.objects.filter(doc_name=image).first()
        print(image_query)
        print(image_name)
        image_query.objects.add(
            file_paths=image_name
        )
        # i += 1
        # print(image_query)
        # if i == 3:
        #     break
        # Doc231and232.objects.filter(doc_name=image).update(
        #     file_paths=image_query
        # )



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start_time = time.time()
        get_image()
        print("--- %s seconds ---" % (time.time() - start_time))