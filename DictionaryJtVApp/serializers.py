from rest_framework import serializers
from .models import Sentence
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

class CommentSeializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'