
from rest_framework import serializers

from my.models import *

class SportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sport
        fields = ['id','name']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name','last_name','born','address']        


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class WinnerSerializer(serializers.ModelSerializer):    
    person = PersonSerializer()
    sport = SportSerializer()
    game = GameSerializer()
    class Meta:
        model = Winner
        fields = '__all__'