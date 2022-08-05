from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import *

from . serializers import *
from . models import *


class Table203ViewSet(viewsets.ModelViewSet):
    queryset = Article200.objects.all()
    serializer_class = Table203Serializer
    permission_classes = (IsAuthenticated,)

    # @action(methods=['get'], detail=True)
    # def brand(self, request, pk=None):
    #     brand = Suppliers200.objects.get(pk=pk)
    #     return Response({'brand': brand.name})