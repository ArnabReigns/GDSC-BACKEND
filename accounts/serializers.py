from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = [
        'id','name','email','gender','phone_number','stream',
        'batch','college_id','linkedin_id','github_id','is_member','uid','password'
        ]


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)