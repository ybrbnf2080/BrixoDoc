from rest_framework import serializers
from . models import *


class Table203Serializer(serializers.ModelSerializer):
    brand_no_id = serializers.SlugRelatedField(read_only=True, slug_field='name')
    country_id = serializers.StringRelatedField(read_only=True, many=True)
    ref_no_id = serializers.StringRelatedField(read_only=True, many=True)
    supers_id = serializers.StringRelatedField(read_only=True, many=True)
    doc_no_id = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Article200
        fields = "__all__"
