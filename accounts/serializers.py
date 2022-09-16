from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = CustomUser
        fields = [
        'id','name','email','gender','phone_number',
        'batch','colelge_id','linkedin_id','github_id','is_member'
        ]