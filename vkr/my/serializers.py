
from rest_framework import serializers

from my.models import Sport

class SportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sport
        fields = ['id','name']