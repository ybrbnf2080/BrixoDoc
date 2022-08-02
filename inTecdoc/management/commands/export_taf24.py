import os
from shutil import rmtree

from django.conf import settings
from django.core.management.base import BaseCommand

from inTecdoc.models import (Supliers_200, Article_200, Country_202, Manufacture_203, Ref_203,
                             Supers_204, CritName_210, Crit_210,
                             Trade_207, Doc_231_232, Lnk, Table_404, Table_410)

COMPANIES = Supliers_200.objects.all()
BASE_DIR = settings.BASE_DIR


def update_dirs():
    if os.path.exists(f'{BASE_DIR}/converted_db'):
        rmtree(f'{BASE_DIR}/converted_db')
    os.mkdir(f'{BASE_DIR}/converted_db')
    for comp in COMPANIES:
        os.mkdir(f'{BASE_DIR}/converted_db/{comp.BrandNo}')


def generate_001(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'001.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).rjust(4, '0'),  # BrandNo
            '1'.rjust(3, '0'),  # TableNo
            '0'.rjust(4, '0'),  # Data Release
            '20220209'.rjust(8, '0'),  # VersionDate
            '1'.rjust(1, '0'),  # Full
            '3870'.rjust(6, '0'),  # ManNo
            COMPANIES.get(BrandNo=brand_no).Name.ljust(20),  # BrandName
            '722'.rjust(4, '0'),  # RefDataVersion
            ''.rjust(4),  # Reserved
            '2.4'.ljust(3),  # Format
            '0'.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_030(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'030.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            ''.ljust(22),  # Reserved
            ''.ljust(4),  # BrandNo
            ''.ljust(3),  # TableNo
            ''.ljust(9),  # TermNo
            ''.ljust(3),  # LangNo
            ''.ljust(60),  # Term
            ''.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_035(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'035.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            ''.ljust(22),  # Reserved
            ''.ljust(4),  # BrandNo
            ''.ljust(3),  # TableNo
            ''.ljust(6),  # TxtModNo
            ''.ljust(3),  # LangNo
            ''.ljust(1),  # Fixed
            ''.ljust(3),  # SeqNo
            ''.ljust(60),  # Text
            ''.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))

#Сделать условие в зависимость от бренда
def generate_040(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'040.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).ljust(4),  # BrandNo
            '40'.ljust(3),  # TableNo
            COMPANIES.get(BrandNo=brand_no).Name.ljust(40),  # Term1
            ''.ljust(40),  # Term2
            'Mamonovskiy pereulok'.ljust(40),  # Street1
            '4 str.1'.ljust(40),  # Street2
            ''.ljust(10),  # POBox
            'RUS'.ljust(3),  # CountryCode
            '123001'.ljust(8),  # PostCode
            ''.ljust(8),  # PostCodePOBox
            ''.ljust(8),  # PostCodeCus
            'Moscow'.ljust(40),  # City1
            ''.ljust(40),  # City2
            '8(800)707-60-97'.ljust(20),  # Phone
            ''.ljust(20),  # Fax
            'feedback@nibk.ru'.ljust(60),  # Email
            'http://www.nibk.ru/'.ljust(60),  # Web
            '1'.ljust(3),  # AdrType
            '0'.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_042(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'042.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).ljust(4),  # BrandNo
            '42'.rjust(3, '0'),  # TableNo
            ''.ljust(3),  # CountryCode
            Doc_231_232.objects.get().rjust(9, '0'),  # DocNo
            ''.ljust(2),  # DocType
            '0'.ljust(1),  # DeleteFlag
        ]
        file.write(''.join(data))


def generate_043(brand_no: str):
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'043.{brand_no}', 'w', encoding='utf-8') as file:
        data = [
            str(brand_no).ljust(4),  # BrandNo
            '43'.ljust(3),  # TableNo
            ''.ljust(3),  # AdrType
            ''.ljust(3),  # CountryCode
            ''.ljust(40),  # Term1
            ''.ljust(40),  # Term2
            ''.ljust(40),  # Street1
            ''.ljust(40),  # Street2
            ''.ljust(10),  # POBox
            ''.ljust(3),  # CountryCode1
            ''.ljust(8),  # PostCode
            ''.ljust(8),  # PostCodePOBox
            ''.ljust(8),  # PostCodeCus
            ''.ljust(40),  # City1
            ''.ljust(40),  # City2
            ''.ljust(20),  # Phone
            ''.ljust(20),  # Fax
            ''.ljust(60),  # Email
            ''.ljust(60),  # Web
            ''.ljust(1),  # AdrType1
        ]
        file.write(''.join(data))


def generate_200(brand_no: str):
    objects = Article_200.objects.filter(BrandNoId__BrandNo=brand_no)
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'200.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.ArtNo.ljust(22),  # ArtNo
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


def generate_201(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'201.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '201'.ljust(3),  # TableNo
                ''.ljust(10),  # Price
                ''.ljust(3),  # PrUnit
                ''.ljust(3),  # PrQuantUnit
                ''.ljust(8),  # ValidFrom
                ''.ljust(8),  # ValidTo
                ''.ljust(3),  # CountryCode
                ''.ljust(3),  # PrType
                ''.ljust(10),  # Reserved
                ''.ljust(3),  # CurCode
                ''.ljust(5),  # DiscGroup
                ''.ljust(1),  # Dicount
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_202(brand_no: str):
    objects = Article_200.objects.filter(BrandNoId__BrandNo=brand_no).prefetch_related('Country')
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'202.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                obj.ArtNo.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '202'.ljust(3),  # TableNo
                # obj.Country,  # CountryCode
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')
            # print('data', data)


def generate_203(brand_no: str):
    objects = Ref_203.objects.filter()
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'203.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '203'.ljust(3),  # TableNo
                ''.ljust(6),  # ManNo
                ''.ljust(3),  # CountryCode
                ''.ljust(22),  # RefNo
                ''.ljust(1),  # Exclude
                ''.ljust(5),  # SortNo
                ''.ljust(1),  # Additive
                ''.ljust(3),  # ReferenceInfo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_204(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'204.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '204'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                ''.ljust(22),  # SupersNo
                ''.ljust(1),  # Exclude
                ''.ljust(5),  # SortNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_205(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'205.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '205'.ljust(3),  # TableNo
                ''.ljust(5),  # PartGenArtNo
                ''.ljust(3),  # SeqNo
                ''.ljust(22),  # PartNo
                ''.ljust(3),  # Quantity
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_206(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'206.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '206'.ljust(3),  # TableNo
                ''.ljust(5),  # Reserved
                ''.ljust(3),  # CountryCode
                ''.ljust(2),  # SortNo
                ''.ljust(3),  # InfType
                ''.ljust(1),  # FirstPage
                ''.ljust(6),  # TXTModNo
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_207(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'207.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '207'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                ''.ljust(35),  # TradeNo
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # FirstPage
                ''.ljust(5),  # SortNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_208(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'208.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '208'.ljust(3),  # TableNo
                ''.ljust(3),  # Reserved
                ''.ljust(5),  # SeqNo
                ''.ljust(3),  # SortNo
                ''.ljust(4),  # CritNo
                ''.ljust(20),  # CritVal
                ''.ljust(1),  # Reserved1
                ''.ljust(3),  # SeqNo1
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_209(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'209.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '209'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                ''.ljust(13),  # GTIN
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_210(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'210.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '210'.ljust(3),  # TableNo
                ''.ljust(5),  # Reserved
                ''.ljust(3),  # CountryCode
                ''.ljust(3),  # SortNo
                ''.ljust(4),  # CritNo
                ''.ljust(20),  # CritVal
                ''.ljust(1),  # FirstPage
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_211(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'211.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '211'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_212(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'212.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '212'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                ''.ljust(5),  # QuantUnit
                ''.ljust(5),  # QuantPerUnit
                ''.ljust(3),  # ArtStat
                ''.ljust(8),  # StatusDat
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_215(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'215.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '215'.ljust(3),  # TableNo
                ''.ljust(3),  # SeqNo
                ''.ljust(3),  # CountryCode
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_217(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'217.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '217'.ljust(3),  # TableNo
                ''.ljust(3),  # SeqNo
                ''.ljust(9),  # DocNo
                ''.ljust(2),  # DocType
                ''.ljust(3),  # LangNo
                ''.ljust(4),  # CoordNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_222(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'222.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '222'.ljust(3),  # TableNo
                ''.ljust(1),  # LnkType
                ''.ljust(6),  # LnkVal
                ''.ljust(3),  # SeqNo
                ''.ljust(3),  # SortNo
                ''.ljust(22),  # AccArtNo
                ''.ljust(3),  # Quantity
                ''.ljust(5),  # AccGenArtNo
                ''.ljust(1),  # Reserved
                ''.ljust(9),  # TermNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_228(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'228.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '228'.ljust(3),  # TableNo
                ''.ljust(3),  # CountryCode
                ''.ljust(3),  # SeqNo1
                ''.ljust(3),  # SortNo1
                ''.ljust(3),  # SeqNo
                ''.ljust(4),  # CritNo
                ''.ljust(20),  # CritVal
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_231(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'231.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # Reserved
                str(brand_no).ljust(4),  # BrandNo
                '231'.ljust(3),  # TableNo
                ''.ljust(9),  # DocNo
                ''.ljust(3),  # LangNo
                ''.ljust(30),  # DocName
                ''.ljust(3),  # DocType
                ''.ljust(3),  # DocTermNorm
                ''.ljust(4),  # Width
                ''.ljust(4),  # Height
                ''.ljust(3),  # Colors
                ''.ljust(2),  # DocType1
                ''.ljust(9),  # TermNo
                ''.ljust(1),  # DeleteFlag
                ''.ljust(300),  # URL
            ]
            file.write(''.join(data) + '\n')


def generate_232(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'232.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '232'.ljust(3),  # TableNo
                ''.ljust(2),  # SortNo
                ''.ljust(3),  # CountryCode
                ''.ljust(1),  # Exclude
                ''.ljust(9),  # DocNo
                ''.ljust(2),  # DocType
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_233(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'233.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                str(brand_no).ljust(4),  # BrandNo
                '233'.ljust(3),  # TableNo
                ''.ljust(9),  # DocNo
                ''.ljust(2),  # DocType
                ''.ljust(4),  # CoordNo
                ''.ljust(3),  # SeqNo
                ''.ljust(3),  # LangNo
                ''.ljust(1),  # Type
                ''.ljust(4),  # X1
                ''.ljust(4),  # Y1
                ''.ljust(4),  # X2
                ''.ljust(4),  # Y2
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_400(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'400.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '400'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(3),  # LnkTargetType
                ''.ljust(9),  # LnkTargetNo
                ''.ljust(9),  # SeqNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_401(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'401.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '401'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(3),  # LnkTargetType
                ''.ljust(9),  # LnkTargetNo
                ''.ljust(9),  # SeqNo
                ''.ljust(2),  # SortNo
                ''.ljust(3),  # CountryCode
                ''.ljust(3),  # InfType
                ''.ljust(1),  # FirstPage
                ''.ljust(6),  # TxtModNo
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_403(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'403.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '403'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(3),  # LnkTargetType
                ''.ljust(9),  # LnkTargetNo
                ''.ljust(9),  # SeqNo
                ''.ljust(3),  # CountryCode
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_404(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'404.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '404'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(3),  # LnkTargetType
                ''.ljust(9),  # LnkTargetNo
                ''.ljust(9),  # SortNo
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_410(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'410.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '410'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(3),  # LnkTargetType
                ''.ljust(9),  # LnkTargetNo
                ''.ljust(9),  # SeqNo
                ''.ljust(3),  # SortNo
                ''.ljust(4),  # CritNo
                ''.ljust(20),  # CritVal
                ''.ljust(1),  # FirstPage
                ''.ljust(3),  # CountryCode
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')


def generate_432(brand_no: str):
    objects = []
    with open(BASE_DIR / 'converted_db' / str(brand_no) / f'432.{brand_no}', 'w', encoding='utf-8') as file:
        for obj in objects:
            data = [
                ''.ljust(22),  # ArtNo
                str(brand_no).ljust(4),  # BrandNo
                '432'.ljust(3),  # TableNo
                ''.ljust(5),  # GenArtNo
                ''.ljust(3),  # LnkTargetType
                ''.ljust(9),  # LnkTargetNo
                ''.ljust(9),  # SeqNo
                ''.ljust(3),  # CountryCode
                ''.ljust(2),  # SortNo
                ''.ljust(9),  # DocNo
                ''.ljust(2),  # DocType
                ''.ljust(1),  # Exclude
                ''.ljust(1),  # DeleteFlag
            ]
            file.write(''.join(data) + '\n')




# def test_get(brand_no: str):
#     objects = Article_200.objects.filter(BrandNoId__BrandNo=brand_no).prefetch_related('Country')
#     with open(BASE_DIR / 'converted_db' / str(brand_no) / f'202.{brand_no}', 'w', encoding='utf-8') as file:
#         for obj in objects:
#             data = [
#                 obj.ArtNo.ljust(22),  # ArtNo
#                 str(brand_no).ljust(4),  # BrandNo
#                 '202'.ljust(3),  # TableNo
#                 obj.Country,  # CountryCode
#                 ''.ljust(1),  # Exclude
#                 ''.ljust(1),  # DeleteFlag
#             ]
#             print('data', data)
#             file.write(''.join(data) + '\n')


# def test_get():
#     objects = Article_200.objects.prefetch_related('Country')
#     for i in objects:
#         print(i)


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_dirs()
        for comp in COMPANIES:
            # test_get(comp.BrandNo)
            # generate_001(comp.BrandNo)
            # generate_030(comp.BrandNo)
            # generate_035(comp.BrandNo)
            # generate_040(comp.BrandNo)
            # generate_042(comp.BrandNo)
            # generate_043(comp.BrandNo)
            # generate_200(comp.BrandNo)
            # generate_201(comp.BrandNo)
            generate_202(comp.BrandNo)
            # generate_203(comp.BrandNo)
            # generate_204(comp.BrandNo)
            # generate_205(comp.BrandNo)
            # generate_206(comp.BrandNo)
            # generate_207(comp.BrandNo)
            # generate_208(comp.BrandNo)
            # generate_209(comp.BrandNo)
            # generate_210(comp.BrandNo)
            # generate_211(comp.BrandNo)
            # generate_212(comp.BrandNo)
            # generate_217(comp.BrandNo)
            # generate_222(comp.BrandNo)
            # generate_228(comp.BrandNo)
            # generate_231(comp.BrandNo)
            # generate_232(comp.BrandNo)
            # generate_233(comp.BrandNo)
            # generate_400(comp.BrandNo)
            # generate_401(comp.BrandNo)
            # generate_403(comp.BrandNo)
            # generate_404(comp.BrandNo)
            # generate_410(comp.BrandNo)
            # generate_432(comp.BrandNo)
