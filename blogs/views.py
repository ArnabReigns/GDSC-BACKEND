from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .models import Blog
from .serialisers import *

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAdminUser])
def blogs_post(request):
    caption = request.data['caption']
    image = request.data['image']
    description = request.data['description']
    link = request.data['link']

    Blog(caption=caption,image=image,description=description,link=link).save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def blogs_get_all(request):
    db = Blog.objects.all()
    serialisers = BlogSerialisers(db,many=True)
    return Response(serialisers.data)