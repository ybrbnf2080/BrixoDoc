from rest_framework import serializers
from .models import *


class Country202Serializer(serializers.ModelSerializer):
    class Meta:
        model = Country202
        fields = [
            'country_code',
            'country_name'
        ]


class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers204
        fields = [
            'supers_no'
        ]


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doc231and232
        fields = [
            'doc_no',
            'doc_name',
            'doc_name',
            'lang_no',
            'doc_type',
            'doc_term_no',
            'doc_type_one',
        ]


class ArticleSerializer(serializers.ModelSerializer):
    country_id = Country202Serializer(many=True)
    supers_id = SupersSerializer(many=True)
    doc_no_id = DocsSerializer(many=True)

    class Meta:
        model = Article200
        fields = [
            'id',
            'art_no',
            'country_id',
            'gen_art_no',
            'brand_no_id',
            'gtin',
            'quant_unit',
            'quant_per_unit',
            'art_stat',
            'status_dat',
            'supers_id',
            'doc_no_id'
        ]

    # def update(self, instance, validated_data):
        # if 'country_id' in validated_data:
        #     country_id_data = validated_data.pop('country_id')
        #     country_id = instance.country_id.all()
        #     country_id = list(country_id)
        #     for country_data in country_id_data:
        #         country = country_id.pop(0)
        #         country.country_code = country_data.get('country_code', country.country_code)
        #         country.country_name = country_data.get('country_name', country.country_name)
        #
        #         country.save()
        #         return instance

        # if 'supers_id' in validated_data:
        #     supers_id_data = validated_data.pop('supers_id')
        #     supers_id = instance.supers_id.all()
        #     supers_id = list(supers_id)
        #     for supers_data in supers_id_data:
        #         supers = supers_id.pop(0)
        #         supers.supers_no = supers_data.get('supers_no', supers.supers_no)
        #
        #         supers.save()
        #         return instance

        # if 'doc_no_id' in validated_data:
        #     doc_no_id_data = validated_data.pop('doc_no_id')
        #     doc_no_id = instance.doc_no_id.all()
        #     doc_no_id = list(doc_no_id)
        #     for doc_data in doc_no_id_data:
        #         doc = doc_no_id.pop(0)
        #         doc.doc_no_id = doc_data.get('doc_name', doc.doc_name)
        #
        #         doc.save()
        #         return instance

#
# class ArticleSerializer(serializers.ModelSerializer):
#     country_id = Country202Serializer(many=True)
#
#     class Meta:
#         model = Article200
#         fields = [
#             'art_no',
#             'gen_art_no',
#             'country_id'
#         ]
