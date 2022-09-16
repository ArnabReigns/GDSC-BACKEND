from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = [
        'id','name','email','gender','phone_number','stream',
        'batch','colelge_id','linkedin_id','github_id','is_member',
        
        ]