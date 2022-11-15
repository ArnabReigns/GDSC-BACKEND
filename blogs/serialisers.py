from rest_framework import serializers
from .models import Blog

class BlogSerialisers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['caption','image','description','link']