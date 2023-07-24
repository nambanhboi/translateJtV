from rest_framework import serializers
from DictionaryJtVApp.models import Sentence, Paragraph

class SentenceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sentence
        fields = '__all__'

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'