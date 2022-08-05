from rest_framework import serializers
from . models import *


class Country202Serializer(serializers.ModelSerializer):
    class Meta:
        model = Country202
        fields = [
            'country_code',
            'country_name'
        ]


class Table203Serializer(serializers.ModelSerializer):
    country_id = Country202Serializer(many=True)
    # brand_no_id = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # # country_id = serializers.StringRelatedField(read_only=True, many=True)
    # ref_no_id = serializers.StringRelatedField(read_only=True, many=True)
    # supers_id = serializers.StringRelatedField(read_only=True, many=True)
    # doc_no_id = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Article200
        fields = [
            'art_no',
            'country_id'
        ]

    def update(self, instance, validated_data):
        if 'country_id' in validated_data:
            country_id_data = validated_data.pop('country_id')
            country_id = instance.country_id.all()
            country_id = list(country_id)
            for country_data in country_id_data:
                country = country_id.pop(0)
                country.country_code = country_data.get('country_code', country.country_code)
                country.country_name = country_data.get('country_name', country.country_name)

                country.save()
                return instance