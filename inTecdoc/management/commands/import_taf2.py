import os
from django.conf import settings
from django.core.management.base import BaseCommand
import time
import pandas as pd
from inTecdoc.models import *

pd.options.mode.chained_assignment = None
BASE_DIR = settings.BASE_DIR


def req_txt():
    data_df_001 = pd.ExcelFile(os.path.join(BASE_DIR, 'ImportTAF/sources_static/BoRSA_TAF24_20220227004.xlsb'),
                               engine='pyxlsb')
    df1 = pd.read_excel(data_df_001, 'Служебный')
    df1.drop(['Unnamed: 11', 'Параметры', 'Unnamed: 7', 'Unnamed: 6',
              'Unnamed: 9', 'Unnamed: 8'
              ], axis=1, inplace=True)
    df1.rename(columns={'Unnamed: 2': 'Name', 'Unnamed: 3': 'position',
                        'Unnamed: 4': 'range'}, inplace=True)

    df1 = df1.drop(index=[0])

    dirname = os.path.join(BASE_DIR, 'ImportTAF/sources_tec/4378/')
    files = os.listdir(dirname)
    temp = map(lambda name: os.path.join(dirname, name), files)
    all_txt = [i.split('/')[-1].split('.')[0] for i in list(temp)]
    return df1


def get_data_in_txt(num):
    # ToDO в 410 есть запятые,
    data_df1 = pd.read_csv(os.path.join(BASE_DIR, f'ImportTAF/sources_tec/4378/{num}.4378'), header=None,
                           sep=";")
    data_df2 = pd.read_csv(os.path.join(BASE_DIR, f'ImportTAF/sources_tec/4630/{num}.4630'), header=None,
                           sep=";")
    data_df3 = pd.read_csv(os.path.join(BASE_DIR, f'ImportTAF/sources_tec/4682/{num}.4682'), header=None,
                           sep=";")
    data_df = pd.concat([data_df1, data_df2, data_df3], ignore_index=True)
    regulations = req_txt().query(f"Структура == '{num}'")
    # print(regulations)
    data_df.rename(columns={0: 'data'}, inplace=True)
    data_df = data_df.data.str.split('', expand=True)
    data_df.fillna(value='', inplace=True)
    res_df = pd.DataFrame()
    for i, row in regulations.iterrows():
        res_df[f'{row["Name"].lower()}'] = ''
        res_df[f'{row["Name"].lower()}'] = data_df.loc[:, row['position'] + 1:row['position'] + row['range']].apply("".join,  axis=1)
    return res_df


def get_data():
    data_df_200 = get_data_in_txt('200')
    data_df_202 = get_data_in_txt('202')

    result_df = data_df_200.merge(data_df_202, how='left',
                                  left_on=['artno'],
                                  right_on=['artno'])

    result_df.rename(columns={'brandno_x': 'brandno'}, inplace=True)

    result_df.drop(['termno', 'batchsize2', 'deleteflag_y', 'selfserv',
                    'matcert', 'remanufact', 'accessory', 'exclude', 'brandno_y',
                    'batchsize1', 'deleteflag_x'], axis=1, inplace=True)

    data_df_211 = get_data_in_txt('211')
    data_df_211 = data_df_211[["artno", "genartno"]]

    result_df = result_df.merge(data_df_211, how='right',
                                left_on=['artno'],
                                right_on=['artno'])

    data_df_209 = get_data_in_txt('209')
    data_df_209 = data_df_209[['artno', "gtin"]]

    result_df = result_df.merge(data_df_209, how='left',
                                left_on=['artno'],
                                right_on=['artno'])

    data_df_212 = get_data_in_txt('212')
    data_df_212 = data_df_212[['artno', "quantunit", 'artstat',
                               'quantperunit', 'statusdat']]

    result_df = result_df.merge(data_df_212, how='left',
                                left_on=['artno'],
                                right_on=['artno'])

    data_df_204 = get_data_in_txt('204')
    data_df_204 = data_df_204[['artno', 'supersno']]
    result_df = result_df.merge(data_df_204, how='left',
                                left_on=['artno'],
                                right_on=['artno'])

    data_df_232 = get_data_in_txt('232')
    data_df_232 = data_df_232[['artno', 'docno']]
    result_df = result_df.merge(data_df_232, how='left',
                                left_on=['artno'],
                                right_on=['artno'])

    data_df_203 = get_data_in_txt('203')
    data_df_203 = data_df_203[['artno', 'manno', 'refno']]
    data_df_203['manno'] = data_df_203['manno'].astype("Int64")
    result_df = result_df.merge(data_df_203, how='left',
                                left_on=['artno'],
                                right_on=['artno'])
    # print(result_df)
    return result_df


def get_manufacturer():
    manufacturer = pd.read_csv(os.path.join(BASE_DIR, 'ImportTAF/sources_static/manufacturer.csv'), header=None, sep=";")
    manufacturer.rename(columns={0: 'man_no', 1: 'short_name', 2: 'term_plain'}, inplace=True)
    manufacturer_res_list = []
    for i, row in manufacturer.iterrows():
        manufacturer_res_list.append(Manufacture203(
            man_no=row['man_no'],
            short_name=row['short_name'],
            term_plain=row['term_plain']
        ))
    Manufacture203.objects.bulk_create(manufacturer_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Manufacturer--------------------')


def get_country():
    path = os.path.join(BASE_DIR, 'ImportTAF/sources_static/country.txt')
    with open(path, "r", encoding='utf-8') as f:
        for line in f:
            try:
                _, created = Country202.objects.get_or_create(
                    country_code=line[0:4],
                    country_name=line[4:]
                )
            except:
                print('Error')
        print('---------------END COUNTRY--------------------')


def get_suppliers():
    data_df_40 = get_data_in_txt('040')
    data_df_40 = data_df_40[['brandno', 'street1', 'street2', 'term1',
                             'web', 'countrycode', 'postcode', 'city1',
                             'phone', 'email'
                             ]]
    data_df_40.rename(columns={'countrycode': 'countrycode_sup'}, inplace=True)

    supplier_res_list = []
    for i, row in data_df_40.iterrows():
        supplier_res_list.append(Suppliers200(
            name=row['term1'],
            brand_no=row['brandno'],
            street=row['street1'],
            country_code=row['countrycode_sup'],
            street_two=row['street2'],
            post_code=row['postcode'],
            city=row['city1'],
            phone=row['phone'],
            email=row['email'],
            web_site=row['web'],
        ))
    Suppliers200.objects.bulk_create(supplier_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Suppliers--------------------')


def get_reference():
    data_df_203 = get_data_in_txt('203')
    data_df_203 = data_df_203[['artno', 'manno', 'refno']]
    data_df_203['manno'] = data_df_203['manno'].astype("Int64")
    data_df_203 = data_df_203.dropna()
    ref_res_list = []
    for i, row in data_df_203.iterrows():
        man_no_id = Manufacture203.objects.filter(man_no=int(row['manno'])).first()
        if man_no_id:
            ref_res_list.append(Ref203(
                    ref_no=row['refno'],
                    man_no_id=man_no_id
                ))
    Ref203.objects.bulk_create(ref_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Reference--------------------')


def get_document():
    data_df_231 = get_data_in_txt('231')
    data_df_231 = data_df_231[['docno', 'doctype', 'doctermnorm',
                               'langno', 'docname', 'doctype1']]
    doc_res_lst = []
    for i, row in data_df_231.iterrows():
        doc_res_lst.append(Doc231and232(
            doc_no=row['docno'],
            doc_name=row['docname'],
            lang_no=row['langno'],
            doc_type=row['doctype'],
            doc_type_one=row['doctype1'],
            doc_term_no=row['doctermnorm'],
        ))
    Doc231and232.objects.bulk_create(doc_res_lst, batch_size=1000, ignore_conflicts=True)
    print('---------------END Document--------------------')


def get_supers():
    super_res_list = []
    data_df_204 = get_data_in_txt('204')
    data_df_204 = data_df_204[['artno', 'supersno']]
    for i, row in data_df_204.iterrows():
        super_res_list.append(Supers204(
            supers_no=row['supersno']
        ))
    Supers204.objects.bulk_create(super_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Supers--------------------')


def get_pre_article():
    test_df = get_data()[get_data()['genartno'].notna()]
    ttt = pd.concat([test_df, get_data()]).drop_duplicates(keep=False)

    test_df = get_data()[get_data()['quantunit'].notna()]
    ttt = pd.concat([test_df, get_data()]).drop_duplicates(keep=False)

    test_df = get_data()[get_data()['quantperunit'].notna()]
    ttt = pd.concat([test_df, get_data()]).drop_duplicates(keep=False)

    test_df = get_data()[get_data()['statusdat'].notna()]
    ttt = pd.concat([test_df, get_data()]).drop_duplicates(keep=False)

    pre_article_df = get_data().drop_duplicates(subset=['artno'])
    pre_article_df['gtin'] = pre_article_df['gtin'].fillna(0)
    pre_article_res_list = []
    for i, row in pre_article_df.iterrows():
        brand_no_id = Suppliers200.objects.filter(brand_no=int(row['brandno'])).first()
        if row['gtin']:
            pre_article_res_list.append(Article200(
                art_no=row['artno'],
                brand_no_id=brand_no_id,
                gen_art_no=row['genartno'],
                gtin=row['gtin'],
                quant_unit=row['quantunit'],
                quant_per_unit=row['quantperunit'],
                status_dat=row['statusdat'],
            ))
        else:
            pre_article_res_list.append(Article200(
                art_no=row['artno'],
                brand_no_id=brand_no_id,
                gen_art_no=row['genartno'],
                quant_unit=row['quantunit'],
                quant_per_unit=row['quantperunit'],
                status_dat=row['statusdat']
            ))
    Article200.objects.bulk_create(pre_article_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END PRE Article--------------------')


def get_article():
    get_data()['countrycode'] = get_data()['countrycode'].fillna('')
    get_data()['supersno'] = get_data()['supersno'].fillna('')
    get_data()['refno'] = get_data()['refno'].fillna('')
    get_data()['docno'] = get_data()['docno'].fillna(0)

    article_res_list = []
    for i, row in get_data().iterrows():
        supers_id = Supers204.objects.filter(supers_no=row['supersno']).first()  # Todo
        ref_no_id = Ref203.objects.filter(ref_no=row['refno']).first()  # Todo
        country = Country202.objects.filter(country_code=row['countrycode']).first()  # Todo
        doc_no_id = Doc231and232.objects.filter(doc_no=row['docno']).first()  # Todo
        article_res_list.append(Article200(
            country_id=country,
            supers_id=supers_id,
            ref_no_id=ref_no_id,
            doc_no_id=doc_no_id
        ))
    Article200.objects.bulk_create(article_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Article--------------------')


def get_criteria():
    criteria = pd.read_csv(os.path.join(BASE_DIR, 'ImportTAF/sources_static/criteria.csv'), header=None, sep=";")
    criteria.rename(columns={0: 'crit_no', 1: 'name', 2: 'description'}, inplace=True)
    criteria_res_list = []
    for i, row in criteria.iterrows():
        criteria_res_list.append(CritVal210(
            crit_no=row['crit_no'],
            name=row['name'],
            description=row['description']
        ))
    CritVal210.objects.bulk_create(criteria_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Criteria--------------------')


def criteria_in_article():
    crit_res_list = []
    data_df_210 = get_data_in_txt('210')
    data_df_210 = data_df_210[['artno', 'critno', 'critval']]
    for i, row in data_df_210.iterrows():
        art_no_id = Article200.objects.filter(art_no=row['artno']).first()
        crit_no_id = CritVal210.objects.filter(crit_no=row['critno']).first()
        crit_res_list.append(Crit210(
            art_no_id=art_no_id,
            crit_no_id=crit_no_id,
            crit_val=row['critval'],
        ))
    Crit210.objects.bulk_create(crit_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Criteria_In_Article--------------------')


def get_trade():
    trade_res_list = []
    data_df_207 = get_data_in_txt('207')
    data_df_207 = data_df_207[['artno', 'tradeno', 'firstpage']]
    for i, row in data_df_207.iterrows():
        art_no_id = Article200.objects.filter(art_no=row['artno']).first()
        trade_res_list.append(Trade207(
            art_no_id=art_no_id,
            trade_no=row['tradeno'],
            first_page=row['firstpage'],
        ))
    Trade207.objects.bulk_create(trade_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Trade--------------------')


def get_lnk():
    lnk_res_list = []
    data_df_400 = get_data_in_txt('400')
    data_df_400 = data_df_400[['artno', 'genartno', 'lnktargettype', 'lnktargetno', 'seqno']]
    for i, row in data_df_400.iterrows():
        art_no_id = Article200.objects.filter(art_no=row['artno']).first()
        lnk_res_list.append(Lnk400(
            art_no_id=art_no_id,
            gen_art_no=row['genartno'],
            lnk_target_type=row['lnktargettype'],
            lnk_target_no=row['lnktargetno'],
            seq_no=row['seqno']
        ))
    Lnk400.objects.bulk_create(lnk_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Lnk--------------------')


def get_table404():
    table404_res_list = []
    data_df_404 = get_data_in_txt('404')
    data_df_404 = data_df_404[['artno', 'genartno', 'lnktargettype', 'lnktargetno']]
    for i, row in data_df_404.iterrows():
        art_no_id = Article200.objects.filter(art_no=row['artno']).first()
        table404_res_list.append(Table404(
            art_no_id=art_no_id,
            gen_art_no=row['genartno'],
            lnk_target_type=row['lnktargettype'],
            lnk_target_no=row['lnktargetno'],
        ))
    Table404.objects.bulk_create(table404_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Table404--------------------')


def get_table410():
    table410_res_list = []
    data_df_410 = get_data_in_txt('410')
    data_df_410 = data_df_410[['artno', 'genartno', 'lnktargettype', 'lnktargetno', 'seqno', 'critno', 'critval', 'firstpage']]
    for i, row in data_df_410.iterrows():
        art_no_id = Article200.objects.filter(art_no=row['artno']).first()
        table410_res_list.append(Table410(
            art_no_id=art_no_id,
            gen_art_no=row['genartno'],
            lnk_target_type=row['lnktargettype'],
            lnk_target_no=row['lnktargetno'],
            seq_no=row['seqno'],
            crit_no=row['critno'],
            crit_val=row['critval'],
            first_page=row['firstpage'],
        ))
    Table410.objects.bulk_create(table410_res_list, batch_size=1000, ignore_conflicts=True)
    print('---------------END Table410--------------------')


def clear_data():
    Suppliers200.objects.all().delete()
    Country202.objects.all().delete()
    Manufacture203.objects.all().delete()
    Ref203.objects.all().delete()
    Supers204.objects.all().delete()
    Doc231and232.objects.all().delete()
    Article200.objects.all().delete()
    CritVal210.objects.all().delete()
    Crit210.objects.all().delete()
    Lnk400.objects.all().delete()
    Table404.objects.all().delete()
    Table410.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        start_time = time.time()
        get_manufacturer()
        get_country()
        get_suppliers()
        get_reference()
        get_document()
        get_supers()
        get_pre_article()
        # get_article()
        get_criteria()
        criteria_in_article()
        get_trade()
        get_lnk()
        get_table404()
        get_table410()
        print("--- %s seconds ---" % (time.time() - start_time))