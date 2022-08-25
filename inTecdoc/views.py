from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.views import APIView

from .serializers import *
from .models import *


class ArticleAPIView(APIView):

    def get(self, request):
        queryset = Article200.objects.all()[:3]
        serializer = ArticleSerializer(queryset, many=True)

        return Response(serializer.data)

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
        queryset = Article200.objects.filter(id=pk)
        serializer = ArticleSerializer(queryset, many=True)

        return Response(serializer.data)



    # queryset = Article200.objects.all()[:3]
    # serializer_class = ArticleSerializer
    #
    # permission_classes = (IsAuthenticated,)

    #
    # @action(methods=['get'], detail=True)
    # def brand(self, request, pk=None):
    #     brand = Suppliers200.objects.get(pk=pk)
    #     return Response({'brand': brand.name})
