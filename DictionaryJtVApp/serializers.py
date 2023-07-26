from rest_framework import serializers
from .models import Sentence,Report,Contribute
from .models import Sentence, CustomerUser

class SentenceSeializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'

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

class reportSeializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ContributetSeializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = '__all__'