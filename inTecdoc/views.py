from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.views import APIView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .serializers import *
from .models import *

from django.core.management import call_command


class ArticleAPIView(APIView):

    def get(self, request):
        nextPage = 1
        previousPage = 1
        chank = request.GET.get('page')
        ditrection = request.GET.get('direction')

        page_from = 0
        page_to = 100

        try:
            query = Chanks.objects
            page = query.all()
            count = page[0].count
        except:
            count = 1
        if chank is None:
            query0 = Chanks.objects.all()
            if not query0:
                Chanks.objects.create(page_from=0, page_to=100, count=count)
            else:
                Chanks.objects.update(page_from=0, page_to=100, count=count)
        elif count == 10 and ditrection == "next":
            query = Chanks.objects
            page = query.all()
            page_from = page[0].page_from
            page_to = page[0].page_to
            query.update(page_from=page_from + 100, page_to=page_to + 100, count=chank)
            query.all()
            page_from = page[0].page_from
            page_to = page[0].page_to
        elif count < 10 and ditrection == "prev":
            query = Chanks.objects
            page = query.all()
            page_from = page[0].page_from
            page_to = page[0].page_to
            if page_from - 10 < 0:
                page_from = 10
                page_to = 100 + 10
            query.update(page_from=page_from - 10, page_to=page_to - 10, count=chank)
            query.all()
            page_from = page[0].page_from
            page_to = page[0].page_to
        elif chank and count < 10:
            query = Chanks.objects
            page = query.all()
            page_from = page[0].page_from
            page_to = page[0].page_to
            query.update(count=chank)

        customers = Article200.objects.all()[page_from:page_to]
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ArticleSerializer(data, context={'request': request}, many=True)

        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        queryset1 = Ref203.objects.filter(art_no_id__in=customers)
        queryset2 = Suppliers200.objects.all().values('brand_no', 'name')
        reference = ReferenceSerializer(queryset1, many=True)

        return Response({'article': serializer.data,
                         "reference": reference.data,
                         'count': paginator.count,
                         'numpages': paginator.num_pages,
                         'brand_no': queryset2,
                         'nextlink': '/api/v1/article/?page=' + str(nextPage),
                         'prevlink': '/api/v1/article/?page=' + str(previousPage),
                         'chank': {"from": page_from, "to": page_to}
                         })

    def post(self, request):
        brand_name = Suppliers200.objects.filter(name=request.data['brand_no_id']['name']).first()
        Article200.objects.update(
            art_no=request.data['art_no'],
            brand_no_id=brand_name,
            gen_art_no=request.data['gen_art_no'],
            quant_unit=request.data['quant_unit'],
            quant_per_unit=request.data['quant_per_unit'],
            art_stat=request.data['art_stat'],
            status_dat=request.data['status_dat'],
            gtin=request.data['gtin'],
        )

        def add_country():
            list_country = request.data['country_id']
            countries = []
            for dicts in list_country:
                country = dicts.get('country_code')
                countries.append(country)
            countries = Country202.objects.filter(country_code__in=countries)
            obj = Article200.objects.filter(art_no=request.data['art_no']).first()
            obj.country_id.set(countries)

        def add_supers():
            list_supers = request.data['supers_id']
            supers = []
            for dicts in list_supers:
                super_one = dicts.get('supers_no')
                supers.append(super_one)
            supers = Supers204.objects.filter(supers_no__in=supers)
            obj = Article200.objects.filter(art_no=request.data['art_no']).first()
            obj.supers_id.set(supers)

        def add_documents():
            list_documents = request.data['doc_no_id']
            documents = []
            for dicts in list_documents:
                document = dicts.get('doc_no')
                documents.append(document)
            documents = Doc231and232.objects.filter(doc_no__in=documents)
            obj = Article200.objects.filter(art_no=request.data['art_no']).first()
            obj.doc_no_id.set(documents)

        add_country()
        add_supers()
        add_documents()
        return Response(request.data)


class ArticleAPIViewItem(APIView):

    def get(self, request, pk):
        queryset1 = Article200.objects.filter(id=pk)
        queryset2 = Crit210.objects.filter(art_no_id__in=queryset1)
        queryset3 = Ref203.objects.filter(art_no_id__in=queryset1)
        queryset4 = Trade207.objects.filter(art_no_id__in=queryset1)
        queryset9 = Supers204.objects.filter(art_no_id__in=queryset1)
        queryset5 = Suppliers200.objects.all().values("name")
        queryset6 = Country202.objects.all()
        queryset7 = CritVal210.objects.all()
        queryset8 = Table404.objects.filter(art_no_id__in=queryset1)
        article = ArticleSerializer(queryset1, many=True)
        crit = CritSerializer(queryset2, many=True)
        reference = ReferenceSerializer(queryset3, many=True)
        trade = TradeSerializer(queryset4, many=True)
        supers = SupersSerializer(queryset9, many=True)
        brands = SuppliersSerializer(queryset5, many=True)
        country = Country202Serializer(queryset6, many=True)
        characteristics = CritValSerializer(queryset7, many=True)
        # applicability =

        serializer = {
            "article": article.data[0],
            "crit": crit.data,
            "reference": reference.data,
            "trade": trade.data,
            "supers": supers.data,
            "brands": brands.data,
            "country": country.data,
            "characteristics": characteristics.data
        }

        return Response(serializer)

    def put(self, request, pk):
        brand_name = Suppliers200.objects.filter(name=request.data['brand_no_id']['name']).first()
        Article200.objects.filter(id=pk).update(
            art_no=request.data['art_no'],
            brand_no_id=brand_name,
            gen_art_no=request.data['gen_art_no'],
            quant_unit=request.data['quant_unit'],
            quant_per_unit=request.data['quant_per_unit'],
            art_stat=request.data['art_stat'],
            status_dat=request.data['status_dat'],
            gtin=request.data['gtin'],
        )

        def update_country():
            list_country = request.data['country_id']
            countries = []
            for dicts in list_country:
                country = dicts.get('label')
                countries.append(country)
            countries = Country202.objects.filter(country_code__in=countries)
            obj = Article200.objects.filter(art_no=request.data['art_no']).first()
            obj.country_id.set(countries)

        def update_supers():
            supers = request.data['supers_id']
            art_no = Article200.objects.filter(art_no=request.data['art_no']).first()
            Supers204.objects.filter(art_no_id=art_no).delete()
            for sup in supers:
                art_no = Article200.objects.filter(art_no=request.data['art_no']).first()
                Supers204.objects.create(
                    supers_no=sup['label'],
                    art_no_id=art_no
                )

        def update_trade():
            trades = request.data['trade_id']
            art_no = Article200.objects.filter(art_no=request.data['art_no']).first()
            Trade207.objects.filter(art_no_id=art_no).delete()
            for trade in trades:
                art_no = Article200.objects.filter(art_no=request.data['art_no']).first()
                Trade207.objects.create(
                    trade_no=trade['label'],
                    art_no_id=art_no
                )

        def update_reference():
            references = request.data['reference']
            art_no = Article200.objects.filter(art_no=request.data['art_no']).first()

            Ref203.objects.filter(art_no_id=art_no).delete()
            for reference in references:
                art_no = Article200.objects.filter(art_no=request.data['art_no']).first()
                man_no = Manufacture203.objects.filter(man_no=reference['man_no_id']['man_no']).first()
                country_code = Country202.objects.filter(country_code=reference['country_code']).first()
                Ref203.objects.create(
                    art_no_id=art_no,
                    man_no_id=man_no,
                    ref_no=reference['ref_no'],
                    country_code_id=country_code,
                )

        def update_documents():
            list_documents = request.data['doc_no_id']
            documents = []
            for dicts in list_documents:
                document = dicts.get('doc_no')
                documents.append(document)
            documents = Doc231and232.objects.filter(doc_no__in=documents)
            obj = Article200.objects.filter(art_no=request.data['art_no']).first()
            obj.doc_no_id.set(documents)

        update_country()
        update_supers()
        update_trade()
        # update_reference()
        # update_documents()
        return Response(request.data)

        # def add_country():
        #     list_country = request.data['country_id']
        #     countries = []
        #     for dicts in list_country:
        #         country = dicts.get('country_code')
        #         countries.append(country)
        #     countries = Country202.objects.filter(country_code__in=countries)
        #     obj = Article200.objects.filter(art_no=request.data['art_no']).first()
        #     obj.country_id.set(countries)


class ReferencesAPIViewItem(APIView):
    def post(self, request, art_no_id):
        references = request.data['reference']
        result = []
        for reference in references:
            art_no = Article200.objects.filter(id=art_no_id).first()
            man_no = Manufacture203.objects.filter(man_no=reference['man_no_id']['man_no']).first()
            country_code = Country202.objects.filter(country_code=reference['country_code']).first()
            if_ref = Ref203.objects.filter(art_no_id=art_no, man_no_id=man_no, ref_no=reference['ref_no'],
                                           country_code_id=country_code)
            if not if_ref:
                Ref203.objects.create(
                    art_no_id=art_no,
                    man_no_id=man_no,
                    ref_no=reference['ref_no'],
                    country_code_id=country_code,
                )
                result = "Success: Референс добавлен"
            else:
                result = "Error: Референс уже существует"
        return Response(result)

    def delete(self, request, art_no_id):
        references = request.data['reference']
        for reference in references:
            art_no = Article200.objects.filter(id=art_no_id).first()
            man_no = Manufacture203.objects.filter(man_no=reference['man_no_id']['man_no']).first()
            country_code = Country202.objects.filter(country_code=reference['country_code']).first()
            Ref203.objects.filter(art_no_id=art_no, man_no_id=man_no, ref_no=reference['ref_no'],
                                  country_code_id=country_code).delete()
        return Response(request.data)


class CharacteristicsAPIViewItem(APIView):
    def post(self, request, art_no_id):
        crits = request.data['crit']
        for crit in crits:
            art_no = Article200.objects.filter(id=art_no_id).first()
            crit_no = CritVal210.objects.filter(crit_no=crit['crit_no_id']['crit_no']).first()
            crit_val = crit['crit_val']
            if_crit = Crit210.objects.filter(art_no_id=art_no, crit_no_id=crit_no, crit_val=crit_val)
            if not if_crit:
                Crit210.objects.create(
                    art_no_id=art_no,
                    crit_no_id=crit_no,
                    crit_val=crit_val
                )
        return Response(request.data)

    def delete(self, request, art_no_id):
        crit = request.data
        print(crit)
        crit_no = CritVal210.objects.filter(crit_no=crit['crit_no_id']['crit_no']).first()
        crit_val = crit['crit_val']
        Crit210.objects.filter(art_no_id=art_no_id, crit_no_id=crit_no, crit_val=crit_val).delete()

        return Response(request.data)

    def put(self, request, art_no_id):
        crit = request.data
        crit_id = crit['id']
        print(crit_id)
        crit_no = CritVal210.objects.filter(crit_no=crit['crit_no']).first()
        print(crit_no)
        crit_val = crit['crit_val']
        Crit210.objects.filter(art_no_id=art_no_id, id=crit_id).update(
            crit_no_id=crit_no,
            crit_val=crit_val,
        )
        return Response(request.data)


class ArticleFilterBrandAPIViewItem(APIView):

    def get(self, request, brand_no):
        queryset1 = Article200.objects.filter(brand_no_id__brand_no=brand_no)[:10]
        article = ArticleSerializer(queryset1, many=True)
        serializer = {"article": article.data}
        return Response(serializer)


class ArticleSearchAPIViewItem(APIView):

    def get(self, request, art_no):
        queryset1 = Article200.objects.filter(art_no__contains=art_no)[:10]
        article = ArticleSearchSerializer(queryset1, many=True)
        serializer = {"article": article.data}
        return Response(serializer)


class GetExportTafAPIView(APIView):

    def get(self, request):
        call_command('export_taf24')
        return Response("success")


class GetImportTafAPIView(APIView):

    def get(self, request):
        call_command('import_taf2')
        return Response("success")

    # queryset = Article200.objects.all()[:3]
    # serializer_class = ArticleSerializer
    #
    # permission_classes = (IsAuthenticated,)

    #
    # @action(methods=['get'], detail=True)
    # def brand(self, request, pk=None):
    #     brand = Suppliers200.objects.get(pk=pk)
    #     return Response({'brand': brand.name})
