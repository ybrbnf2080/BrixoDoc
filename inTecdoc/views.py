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
        serialezer = ArticleSerializer(queryset, many=True)

        return Response(serialezer.data)

    def post(self, request):
        art_no = request.data['art_no']
        country_id = request.data['country_id']
        Article200.objects.create(
            art_no=art_no
        )
        return Response({"art_no": art_no})


class ArticleAPIViewItem(APIView):

    def get(self, request, pk):
        print(pk)
        queryset = Article200.objects.filter(id=pk)
        serialezer = ArticleSerializer(queryset, many=True)

        return Response(serialezer.data)



    # queryset = Article200.objects.all()[:3]
    # serializer_class = ArticleSerializer
    #
    # permission_classes = (IsAuthenticated,)

    #
    # @action(methods=['get'], detail=True)
    # def brand(self, request, pk=None):
    #     brand = Suppliers200.objects.get(pk=pk)
    #     return Response({'brand': brand.name})
