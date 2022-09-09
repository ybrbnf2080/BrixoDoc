import os
import shutil
from shutil import rmtree

from django.db.models import *
from django.conf import settings
from django.core.management.base import BaseCommand
import time
import zipfile
from inTecdoc.models import *

COMPANIES = Suppliers200.objects.all()
BASE_DIR = settings.BASE_DIR


def update_dirs():
    if os.path.exists(f'{BASE_DIR}/converted_db'):
        rmtree(f'{BASE_DIR}/converted_db')
    os.mkdir(f'{BASE_DIR}/converted_db')
    for comp in COMPANIES:
        os.mkdir(f'{BASE_DIR}/converted_db/{comp.brand_no}')


def generate_001(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'001.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).rjust(4, '0'),  # BrandNo
            '1'.rjust(3, '0'),  # TableNo
            str(COMPANIES.get(brand_no=brand_no).data_release).rjust(4, '0'),  # Data Release
            str(COMPANIES.get(brand_no=brand_no).version_date).rjust(8, '0'),  # VersionDate
            str(COMPANIES.get(brand_no=brand_no).full).rjust(1, '0'),  # Full
            str(COMPANIES.get(brand_no=brand_no).man_no).rjust(6, '0'),  # ManNo
            COMPANIES.get(brand_no=brand_no).name.ljust(20),  # BrandName
            str(COMPANIES.get(brand_no=brand_no).ref_data_version).rjust(4, '0'),  # RefDataVersion
            ''.rjust(4),  # Reserved
            '2.4'.ljust(3),  # Format
            '0'.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_040(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'040.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).ljust(4),  # BrandNo
            '40'.rjust(3, '0'),  # TableNo
            str(COMPANIES.get(brand_no=brand_no).term1).ljust(40),  # Term1
            ''.ljust(40),  # Term2
            str(COMPANIES.get(brand_no=brand_no).street).ljust(40),  # Street1
            str(COMPANIES.get(brand_no=brand_no).street_two).ljust(40),  # Street2
            ''.ljust(10),  # POBox
            str(COMPANIES.get(brand_no=brand_no).country_code).ljust(3),  # CountryCode
            str(COMPANIES.get(brand_no=brand_no).post_code).ljust(8),  # PostCode
            str(COMPANIES.get(brand_no=brand_no).post_code_pobox).ljust(8),  # PostCodePOBox
            str(COMPANIES.get(brand_no=brand_no).post_code_cus).ljust(8),  # PostCodeCus
            str(COMPANIES.get(brand_no=brand_no).city).ljust(40),  # City1
            ''.ljust(40),  # City2
            str(COMPANIES.get(brand_no=brand_no).phone).ljust(20),  # Phone
            ''.ljust(20),  # Fax
            str(COMPANIES.get(brand_no=brand_no).email).ljust(60),  # Email
            str(COMPANIES.get(brand_no=brand_no).web_site).ljust(60),  # Web
            str(COMPANIES.get(brand_no=brand_no).adr_type).rjust(3, '0'),  # AdrType
            '0'.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_042(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'042.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).ljust(4),  # BrandNo
            '42'.rjust(3, '0'),  # TableNo
            ''.ljust(3),  # CountryCode
            str(COMPANIES.get(brand_no=brand_no).doc_no).rjust(9, '0'),  # DocNo
            str(COMPANIES.get(brand_no=brand_no).doc_type).rjust(2, '0'),  # DocType
            '0'.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_200(brand_no: str):
    objects = Article200.objects.filter(brand_no_id__brand_no=brand_no)
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'200.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.art_no.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '200'.ljust(3),  # TableNo
                ''.ljust(9),  # TermNo
                '0'.ljust(1),  # SelfServ
                '0'.ljust(1),  # MatCert
                '0'.ljust(1),  # Remanufact
                '0'.ljust(1),  # Accessory
                ''.ljust(5),  # BatchSize1
                ''.ljust(5),  # BatchSize2
                '0'.ljust(1),  # DeleteFlag

            ]
            file.write(''.join(data) + '\n')


def generate_202(brand_no: str):  # Вопрос в последовательности
    objects = Article200.objects.filter(brand_no_id__brand_no=brand_no, country_id__country_code__isnull=False) \
        .values('art_no', 'country_id__country_code')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'202.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.get('art_no').ljust(22, ' '),  # ArtNo
                str(brand_no).rjust(4, '0'),  # BrandNo
                '202'.ljust(3),  # TableNo
                str(obj.get('country_id__country_code')).ljust(3),  # CountryCode
                '0'.ljust(1),  # Exclude
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_203(brand_no: str):
    objects = Ref203.objects.filter(art_no_id__brand_no_id__brand_no=brand_no) \
        .values('art_no_id__art_no', 'man_no_id__man_no', 'ref_no', 'country_code_id')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'203.{brand_no}', 'w', encoding='utf-8') as file:
        art_sort_no = []
        sort_no = 0
        for obj in objects:
            art_no = obj.get('art_no_id__art_no').strip()
            if art_no in art_sort_no:
                art_sort_no.append(art_no)
                sort_no += 1
            else:
                art_sort_no.clear()
                art_sort_no.append(art_no)
                sort_no = 1
            data = [
                obj.get('art_no_id__art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '203'.ljust(3),  # TableNo
                str(obj.get('man_no_id__man_no')).rjust(6, '0'),  # ManNo
                str(obj.get('country_code_id')).rjust(3, '0'),  # CountryCode
                str(obj.get('ref_no')).ljust(22),  # RefNo
                '0'.ljust(1),  # Exclude
                str(sort_no).rjust(5, '0'),  # SortNo
                '0'.ljust(1),  # Additive
                ''.ljust(3),  # ReferenceInfo
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_204(brand_no: str):  # Вопрос в последовательности
    objects = Supers204.objects.filter(art_no_id__brand_no_id__brand_no=brand_no) \
        .values('art_no_id__art_no', 'supers_no')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'204.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                str(obj.get('art_no_id__art_no')).ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '204'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                str(obj.get('supers_no')).ljust(22),  # SupersNo
                '0'.ljust(1),  # Exclude
                '1'.rjust(5, '0'),  # SortNo
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_207(brand_no: str):
    objects = Trade207.objects.filter(art_no_id__brand_no_id__brand_no=brand_no).values('art_no_id__art_no', 'trade_no',
                                                                                        'first_page')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'207.{brand_no}', 'w', encoding='utf-8') as file:
        art_sort_no = []
        sort_no = 0
        for obj in objects:
            art_no = obj.get('art_no_id__art_no').strip()
            if art_no in art_sort_no:
                art_sort_no.append(art_no)
                sort_no += 1
            else:
                art_sort_no.clear()
                art_sort_no.append(art_no)
                sort_no = 1
            data = [
                str(obj.get('art_no_id__art_no')).ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '207'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                str(obj.get('trade_no')).ljust(35),  # TradeNo
                '0'.ljust(1),  # Exclude
                str(obj.get('first_page')).ljust(1),  # FirstPage
                str(sort_no).rjust(5, '0'),  # SortNo
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_209(brand_no: str):  # Уникален ли GTIN? в исходнике 2 шт RN1025 с разными gtin
    objects = Article200.objects.filter(brand_no_id__brand_no=brand_no, gtin__isnull=False).values('art_no', 'gtin')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'209.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                str(obj.get('art_no')).ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '209'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                str(obj.get('gtin')).rjust(13, '0'),  # GTIN
                '0'.ljust(1),  # Exclude
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_210(brand_no: str):
    objects = Crit210.objects.filter(art_no_id__brand_no_id__brand_no=brand_no).values('art_no_id__art_no',
                                                                                       'crit_no_id__crit_no',
                                                                                       'crit_val')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'210.{brand_no}', 'w', encoding='utf-8') as file:
        art_sort_no = []
        sort_no = 0
        for obj in objects:
            art_no = obj.get('art_no_id__art_no').strip()
            if art_no in art_sort_no:
                art_sort_no.append(art_no)
                sort_no += 1
            else:
                art_sort_no.clear()
                art_sort_no.append(art_no)
                sort_no = 1
            data = [
                str(obj.get('art_no_id__art_no')).ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '210'.ljust(3),  # TableNo
                ''.ljust(5),  # Reserved
                ''.ljust(3),  # CountryCode
                str(sort_no).rjust(3, '0'),  # SortNo
                str(obj.get('crit_no_id__crit_no')).rjust(4, '0'),  # CritNo
                str(obj.get('crit_val')).ljust(20),  # CritVal
                '1'.ljust(1),  # FirstPage
                '0'.ljust(1),  # Exclude
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_211(brand_no: str):
    objects = Article200.objects.filter(brand_no_id__brand_no=brand_no).values('art_no', 'gen_art_no')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'211.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.get('art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '211'.ljust(3),  # TableNo
                str(obj.get('gen_art_no')).rjust(5, '0'),  # GenArtNo
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_212(brand_no: str):
    objects = Article200.objects.filter(brand_no_id__brand_no=brand_no).values('art_no', 'quant_unit', 'quant_per_unit',
                                                                               'art_stat', 'status_dat')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'212.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.get('art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '212'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                str(obj.get('quant_unit')).rjust(5, '0'),  # QuantUnit
                str(obj.get('quant_per_unit')).rjust(5, '0'),  # QuantPerUnit
                str(obj.get('art_stat')).rjust(3, '0'),  # ArtStat
                str(obj.get('status_dat')).rjust(8, '0'),  # StatusDat
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_zero_file(brand_no: str):
    # brand_no = Suppliers200.objects.filter(brand_no=brand_no)
    file_030 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'030.{brand_no}', 'w', encoding='utf-8')
    file_035 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'035.{brand_no}', 'w', encoding='utf-8')
    file_043 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'043.{brand_no}', 'w', encoding='utf-8')
    file_201 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'201.{brand_no}', 'w', encoding='utf-8')
    file_205 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'205.{brand_no}', 'w', encoding='utf-8')
    file_206 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'206.{brand_no}', 'w', encoding='utf-8')
    file_208 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'208.{brand_no}', 'w', encoding='utf-8')
    file_213 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'213.{brand_no}', 'w', encoding='utf-8')
    file_214 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'214.{brand_no}', 'w', encoding='utf-8')
    file_215 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'215.{brand_no}', 'w', encoding='utf-8')
    file_216 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'216.{brand_no}', 'w', encoding='utf-8')
    file_217 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'217.{brand_no}', 'w', encoding='utf-8')
    file_222 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'222.{brand_no}', 'w', encoding='utf-8')
    file_228 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'228.{brand_no}', 'w', encoding='utf-8')
    file_233 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'233.{brand_no}', 'w', encoding='utf-8')
    file_401 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'401.{brand_no}', 'w', encoding='utf-8')
    file_402 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'402.{brand_no}', 'w', encoding='utf-8')
    file_403 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'403.{brand_no}', 'w', encoding='utf-8')
    file_432 = open(BASE_DIR / 'converted_db' / str(brand_no) / f'432.{brand_no}', 'w', encoding='utf-8')


def generate_231(brand_no: str):  # Не подхватывает Логотип
    objects = Doc231and232.objects.filter(doc_no_article__brand_no_id__brand_no=brand_no).values('doc_no',
                                                                                                 'lang_no',
                                                                                                 'doc_name',
                                                                                                 'doc_type',
                                                                                                 'doc_term_no',
                                                                                                 'doc_type_one')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'231.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # Reserved
                str(brand_no).ljust(4),  # BrandNo
                '231'.ljust(3),  # TableNo
                str(obj.get('doc_no')).rjust(9, '0'),  # DocNo
                str(obj.get('lang_no')).rjust(3, '0'),  # LangNo
                str(obj.get('doc_name')).ljust(30),  # DocName
                str(obj.get('doc_type')).rjust(3, '0'),  # DocType
                str(obj.get('doc_term_no')).rjust(3, '0'),  # DocTermNorm
                ''.ljust(4),  # Width
                ''.ljust(4),  # Height
                ''.ljust(3),  # Colors
                str(obj.get('doc_type_one')).rjust(2, '0'),  # DocType1
                ''.ljust(9),  # TermNo
                '0'.ljust(1),  # DeleteFlag
                ''.ljust(300),  # URL
            ]
            file.write(''.join(data) + '\n')


def generate_232(brand_no: str):  # Порядок сортировки
    objects = Article200.objects.filter(brand_no_id__brand_no=brand_no, doc_no_id__doc_no__isnull=False).values(
        'art_no', 'doc_no_id__doc_no',
        'doc_no_id__doc_type')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'232.{brand_no}', 'w', encoding='utf-8') as file:
        art_sort_no = []
        sort_no = 0
        for obj in objects:
            art_no = obj.get('art_no').strip()
            if art_no in art_sort_no:
                art_sort_no.append(art_no)
                sort_no += 1
            else:
                art_sort_no.clear()
                art_sort_no.append(art_no)
                sort_no = 1
            data = [
                obj.get('art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '232'.ljust(3),  # TableNo
                str(sort_no).rjust(2, '0'),  # SortNo
                ''.ljust(3),  # CountryCode
                '0'.ljust(1),  # Exclude
                str(obj.get('doc_no_id__doc_no')).rjust(9, '0'),  # DocNo
                str(obj.get('doc_no_id__doc_type')).rjust(2, '0'),  # DocType
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_400(brand_no: str):
    objects = Lnk400.objects.filter(art_no_id__brand_no_id__brand_no=brand_no).values('gen_art_no', 'lnk_target_type',
                                                                                      'lnk_target_no',
                                                                                      'seq_no',
                                                                                      'art_no_id__art_no')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'400.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.get('art_no_id__art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '400'.ljust(3),  # TableNo
                str(obj.get('gen_art_no')).rjust(5, '0'),  # GenArtNo
                str(obj.get('lnk_target_type')).rjust(3, '0'),  # LnkTargetType
                str(obj.get('lnk_target_no')).rjust(9, '0'),  # LnkTargetNo
                str(obj.get('seq_no')).rjust(9, '0'),  # SeqNo
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_404(brand_no: str):
    objects = Table404.objects.filter(art_no_id__brand_no_id__brand_no=brand_no).values('art_no_id__art_no',
                                                                                        'gen_art_no',
                                                                                        'lnk_target_no',
                                                                                        'lnk_target_type', 'sort_no')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'404.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.get('art_no_id__art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '404'.ljust(3),  # TableNo
                str(obj.get('gen_art_no')).rjust(5, '0'),  # GenArtNo
                str(obj.get('lnk_target_type')).rjust(3, '0'),  # LnkTargetType
                str(obj.get('lnk_target_no')).rjust(9, '0'),  # LnkTargetNo
                str(obj.get('sort_no')).rjust(9, '0'),  # SortNo
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_410(brand_no: str):
    objects = Table410.objects.filter(art_no_id__brand_no_id__brand_no=brand_no).values('art_no_id__art_no',
                                                                                        'gen_art_no',
                                                                                        'lnk_target_type',
                                                                                        'lnk_target_no',
                                                                                        'seq_no',
                                                                                        'crit_no',
                                                                                        'crit_val',
                                                                                        'first_page',
                                                                                        'sort_no')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'410.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.get('art_no_id__art_no').ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '410'.ljust(3),  # TableNo
                str(obj.get('gen_art_no')).rjust(5, '0'),  # GenArtNo
                str(obj.get('lnk_target_type')).rjust(3, '0'),  # LnkTargetType
                str(obj.get('lnk_target_no')).rjust(9, '0'),  # LnkTargetNo
                str(obj.get('seq_no')).rjust(9, '0'),  # SeqNo
                str(obj.get('sort_no')).rjust(3, '0'),  # SortNo
                str(obj.get('crit_no')).rjust(4, '0'),  # CritNo
                str(obj.get('crit_val')).ljust(20),  # CritVal
                str(obj.get('first_page')).ljust(1),  # FirstPage
                ''.ljust(3),  # CountryCode
                '0'.ljust(1),  # Exclude
                '0'.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def arch():
    now_date = time.time()
    backup_folders = BASE_DIR / 'converted_db'
    arch_name = "backup_" + str(now_date)

    shutil.make_archive(arch_name, 'zip', backup_folders)


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_dirs()
        for comp in COMPANIES:
            start_time = time.time()
            generate_zero_file(comp.brand_no)
            generate_001(comp.brand_no)
            generate_040(comp.brand_no)
            generate_042(comp.brand_no)
            generate_200(comp.brand_no)
            generate_202(comp.brand_no)
            generate_203(comp.brand_no)
            generate_204(comp.brand_no)
            generate_207(comp.brand_no)
            generate_209(comp.brand_no)
            generate_210(comp.brand_no)
            generate_211(comp.brand_no)
            generate_212(comp.brand_no)
            generate_231(comp.brand_no)
            generate_232(comp.brand_no)
            generate_400(comp.brand_no)
            generate_404(comp.brand_no)
            generate_410(comp.brand_no)
            print("--- %s seconds ---" % (time.time() - start_time))
        arch()

