from rest_framework import serializers
<<<<<<< HEAD
from .models import Sentence
from .models import User
from .models import Comment


=======
from .models import Sentence, CustomerUser
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b

class SentenceSeializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'

<<<<<<< HEAD
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

class CommentSeializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
=======
# class CustomerUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomerUser
#         fields = ('id', 'username', 'is_active', 'is_staff')

class CustomerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['username', 'password', 'is_active', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Tránh lưu trường password trực tiếp vào model
        password = validated_data.pop('password')
        user = CustomerUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class CustomerUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b
