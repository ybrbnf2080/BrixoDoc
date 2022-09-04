from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.views import APIView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .serializers import *
from .models import *


class ArticleAPIView(APIView):

    def get(self, request):
        nextPage = 1
        previousPage = 1
        chank = request.GET.get('page')

        _from = 0
        _to = 100
        if chank == None:
            _from = 0
            _to = 100
        elif int(chank) <= 9:
            _from = 0
            _to = 100
        else:
            _from = _from + 100
            _to = _to + 100
        print("chank ", chank, " from ", _from, " to ", _to)
        customers = Article200.objects.all()[_from:_to]
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
                         'chank': {"from": _from, "to": _to}
                         })

    def post(self, request):
        brand_name = Suppliers200.objects.filter(name=request.data['brand_no_id']['name']).first()
        Article200.objects.create(
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
        queryset5 = Suppliers200.objects.all().values("name")
        queryset6 = Country202.objects.all()
        queryset7 = CritVal210.objects.all()
        queryset8 = Table404.objects.filter(art_no_id__in=queryset1)
        article = ArticleSerializer(queryset1, many=True)
        crit = CritSerializer(queryset2, many=True)
        reference = ReferenceSerializer(queryset3, many=True)
        trade = TradeSerializer(queryset4, many=True)
        brands = SuppliersSerializer(queryset5, many=True)
        country = Country202Serializer(queryset6, many=True)
        characteristics = CritValSerializer(queryset7, many=True)
        # applicability =

        serializer = {
            "article": article.data[0],
            "crit": crit.data,
            "reference": reference.data,
            "trade": trade.data,
            "brands": brands.data,
            "country": country.data,
            "characteristics": characteristics.data
        }

        return Response(serializer)


class ArticleFilterBrandAPIViewItem(APIView):

    def get(self, request, brand_no):
        queryset1 = Article200.objects.filter(brand_no_id__brand_no=brand_no)[:10]
        article = ArticleSerializer(queryset1, many=True)
        serializer = {"article": article.data}
        return Response(serializer)

    # queryset = Article200.objects.all()[:3]
    # serializer_class = ArticleSerializer
    #
    # permission_classes = (IsAuthenticated,)

    #
    # @action(methods=['get'], detail=True)
    # def brand(self, request, pk=None):
    #     brand = Suppliers200.objects.get(pk=pk)
    #     return Response({'brand': brand.name})
