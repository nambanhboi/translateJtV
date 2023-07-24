from rest_framework import serializers
from .models import Sentence,Report,Contribute

class SentenceSeializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'

class reportSeializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ContributetSeializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = '__all__'