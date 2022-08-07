import os
from django.conf import settings
from django.core.management.base import BaseCommand
import time
import pandas as pd
from inTecdoc.models import *

pd.options.mode.chained_assignment = None
BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start_time = time.time()
        data_df_001 = pd.ExcelFile(os.path.join(BASE_DIR, 'ImportTAF/sources_static/BoRSA_TAF24_20220227004.xlsb'), engine='pyxlsb')
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

        # print(all_txt)

        def get_data_in_txt(num):
            # ToDO в 410 есть запятые,
            data_df1 = pd.read_csv(os.path.join(BASE_DIR, f'ImportTAF/sources_tec/4378/{num}.4378'), header=None, sep=";")
            data_df2 = pd.read_csv(os.path.join(BASE_DIR, f'ImportTAF/sources_tec/4630/{num}.4630'), header=None, sep=";")
            data_df3 = pd.read_csv(os.path.join(BASE_DIR, f'ImportTAF/sources_tec/4682/{num}.4682'), header=None, sep=";")
            data_df = pd.concat([data_df1, data_df2, data_df3], ignore_index=True)
            regulations = df1.query(f"Структура == '{num}'")
            # print(regulations)
            data_df.rename(columns={0: 'data'}, inplace=True)
            data_df = data_df.data.str.split('', expand=True)
            data_df.fillna(value='', inplace=True)
            res_df = pd.DataFrame()
            for i, row in regulations.iterrows():
                res_df[f'{row["Name"].lower()}'] = ''
                res_df[f'{row["Name"].lower()}'] = data_df.loc[:,
                                                   row['position'] + 1:row['position'] + row['range']].apply("".join,
                                                                                                             axis=1)
            # print(num)
            # print(res_df)
            return res_df

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

        '''Manufacturer'''
        # manufacturer = pd.read_csv(os.path.join(BASE_DIR, 'ImportTAF/sources_static/manufacturer.csv'), header=None, sep=";")
        # manufacturer.rename(columns={0: 'man_no', 1: 'short_name', 2: 'term_plain'}, inplace=True)
        # manufacturer_res_list = []
        # for i, row in manufacturer.iterrows():
        #     manufacturer_res_list.append(Manufacture203(
        #         man_no=row['man_no'],
        #         short_name=row['short_name'],
        #         term_plain=row['term_plain']
        #     ))
        # Manufacture203.objects.bulk_create(manufacturer_res_list, batch_size=1000, ignore_conflicts=True)
        '''---------------END Manufacturer--------------------'''

        ''' COUNTRY '''
        # def get_country():
        #     path = os.path.join(BASE_DIR, 'ImportTAF/sources_static/country.txt')
        #     with open(path, "r", encoding='utf-8') as f:
        #         for line in f:
        #             try:
        #                 _, created = Country202.objects.get_or_create(
        #                     country_code=line[0:4],
        #                     country_name=line[4:]
        #                 )
        #             except:
        #                 print('Error')
        #     print('------add Country--------')
        # get_country()
        '''----------------------END COUNTRY--------------------------------------'''

        '''Suppliers200'''
        # data_df_40 = get_data_in_txt('040')
        # data_df_40 = data_df_40[['brandno', 'street1', 'street2', 'term1',
        #                          'web', 'countrycode', 'postcode', 'city1',
        #                          'phone', 'email'
        #                          ]]
        # data_df_40.rename(columns={'countrycode': 'countrycode_sup'}, inplace=True)
        #
        # supplier_res_list = []
        # for i, row in data_df_40.iterrows():
        #     supplier_res_list.append(Suppliers200(
        #         name=row['term1'],
        #         brand_no=row['brandno'],
        #         street=row['street1'],
        #         country_code=row['countrycode_sup'],
        #         street_two=row['street2'],
        #         post_code=row['postcode'],
        #         city=row['city1'],
        #         phone=row['phone'],
        #         email=row['email'],
        #         web_site=row['web'],
        #     ))
        # Suppliers200.objects.bulk_create(supplier_res_list, batch_size=1000, ignore_conflicts=True)
        '''------------------------END Suppliers200-------------------------------------'''

        '''REFERENCE'''
        # data_df_203 = get_data_in_txt('203')
        # data_df_203 = data_df_203[['artno', 'manno', 'refno']]
        # data_df_203['manno'] = data_df_203['manno'].astype("Int64")
        # print(data_df_203)
        # data_df_203 = data_df_203.dropna()
        # print(data_df_203)
        # ref_res_list = []
        # c = 0
        # for i, row in data_df_203.iterrows():
        #     c += 1
        #     man_no_id = Manufacture203.objects.filter(man_no=int(row['manno'])).first()
        #     if man_no_id:
        #         print(c, man_no_id)
        #         ref_res_list.append(Ref203(
        #                 ref_no=row['refno'],
        #                 man_no_id=man_no_id
        #             ))
        # Ref203.objects.bulk_create(ref_res_list, batch_size=1000, ignore_conflicts=True)
        '''----------- END REFERENCE ---------------'''

        '''DOC'''
        # data_df_231 = get_data_in_txt('231')
        # data_df_231 = data_df_231[['docno', 'doctype', 'doctermnorm',
        #                            'langno', 'docname', 'doctype1']]
        # doc_res_lst = []
        # for i, row in data_df_231.iterrows():
        #     doc_res_lst.append(Doc231and232(
        #         doc_no=row['docno'],
        #         doc_name=row['docname'],
        #         lang_no=row['langno'],
        #         doc_content_type=row['doctype'],
        #         doc_type=row['doctype1'],
        #         doc_term_no=row['doctermnorm'],
        #     ))
        # Doc231and232.objects.bulk_create(doc_res_lst, batch_size=1000, ignore_conflicts=True)
        '''------------END DOC--------------'''

        '''SUPER'''
        # super_res_list = []
        # data_df_204 = get_data_in_txt('204')
        # data_df_204 = data_df_204[['artno', 'supersno']]
        # for i, row in data_df_204.iterrows():
        #     super_res_list.append(Supers204(
        #         supers_no=row['supersno']
        #     ))
        # Supers204.objects.bulk_create(super_res_list, batch_size=1000, ignore_conflicts=True)
        '''------------END SUPER--------------'''

        '''PRE ARTICLE'''
        # test_df = result_df[result_df['genartno'].notna()]
        # ttt = pd.concat([test_df, result_df]).drop_duplicates(keep=False)
        # print(ttt)
        #
        # test_df = result_df[result_df['quantunit'].notna()]
        # ttt = pd.concat([test_df, result_df]).drop_duplicates(keep=False)
        # print(ttt)
        #
        # test_df = result_df[result_df['quantperunit'].notna()]
        # ttt = pd.concat([test_df, result_df]).drop_duplicates(keep=False)
        # print(ttt)
        #
        # test_df = result_df[result_df['statusdat'].notna()]
        # ttt = pd.concat([test_df, result_df]).drop_duplicates(keep=False)
        # print(ttt)

        # pre_article_df = result_df.drop_duplicates(subset=['artno'])
        # pre_article_df['gtin'] = pre_article_df['gtin'].fillna(0)
        # pre_artc_res_list = []
        # for i, row in pre_article_df.iterrows():
        #     brand_no_id = Suppliers200.objects.filter(brand_no=int(row['brandno'])).first()
        #     if row['gtin']:
        #         pre_artc_res_list.append(Article200(
        #             art_no=row['artno'],
        #             brand_no_id=brand_no_id,
        #             gen_art_no=row['genartno'],
        #             gtin=row['gtin'],
        #             quant_unit=row['quantunit'],
        #             quant_per_unit=row['quantperunit'],
        #             status_dat=row['statusdat'],
        #         ))
        #     else:
        #         pre_artc_res_list.append(Article200(
        #             art_no=row['artno'],
        #             brand_no_id=brand_no_id,
        #             gen_art_no=row['genartno'],
        #             quant_unit=row['quantunit'],
        #             quant_per_unit=row['quantperunit'],
        #             status_dat=row['statusdat']
        #         ))
        # Article200.objects.bulk_create(pre_artc_res_list, batch_size=1000, ignore_conflicts=True)
        '''-----------END PRE ARTICLE--------------'''

        '''ARTICLE'''

        result_df['countrycode'] = result_df['countrycode'].fillna('')
        result_df['supersno'] = result_df['supersno'].fillna('')
        result_df['refno'] = result_df['refno'].fillna('')
        result_df['docno'] = result_df['docno'].fillna(0)

        ref_res_list = []
        count = 0

        for i, row in result_df.iterrows():
            count += 1
            # country_id = Country202.objects.filter(country_code=row['countrycode']).first()  # Todo
            country_id = Article200.objects.filter(art_no=row['artno']).first()  # Todo
            print(country_id)

            # supers_id = Supers204.objects.filter(supers_no=row['supersno']).first()  # Todo
            # ref_no_id = Ref203.objects.filter(ref_no=row['refno']).first()  # Todo
            # doc_no_id = Doc231and232.objects.filter(doc_no=row['docno']).first()  # Todo
            # ref_res_list.append(Article200(
            #     country_id=country_id,
            #     supers_id=supers_id,
            #     ref_no_id=ref_no_id,
            #     doc_no_id=doc_no_id
            # ))
            #
            #
            # print(count)
            # if count == 1000:
            #     break
        Article200.objects.bulk_create(ref_res_list, batch_size=1000, ignore_conflicts=True)

        '''-----------END RESULT--------------'''

        print("--- %s seconds ---" % (time.time() - start_time))
        self.stdout.write('')
