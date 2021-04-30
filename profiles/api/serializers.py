from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Consumer,Moderator


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username','email','password']
        write_only_fields = ('password','username' )

class ModeratorSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    class Meta:
        model = Moderator
        fields = ['contact_number','user','tasks_completed','efficiency']
    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        moderator = Moderator.objects.create(**validated_data,user=user)
        return moderator

class ConsumerSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)
    class Meta:
        model = Consumer
        fields = ['id','contact_number','user','tasks_given']
    def create(self,validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        consumer = Consumer.objects.create(**validated_data,user=user)
        return consumer