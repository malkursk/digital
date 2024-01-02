from rest_framework import serializers

from my.models import Test

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"    