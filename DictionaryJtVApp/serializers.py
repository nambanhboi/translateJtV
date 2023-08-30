from rest_framework import serializers
from .models import Sentence,Report,Contribute
from .models import User
from .models import Comment

class SentenceSeializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

class CommentSerialvizer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class reportSeializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'typeName', 'user','sentence']

class ContributetSeializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = '__all__'