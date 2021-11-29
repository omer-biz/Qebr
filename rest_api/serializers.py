from sites.models import Deceased, Afocha
from rest_framework import serializers

class DeceasedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deceased
        fields = ['efname', 'elname', 'role_num', 'gender', 'dod', 'grave_number',
                  'afocha_name', 'qebele', 'lon', 'lat']

class AfochaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Afocha
        fields = ['name']
