from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from api.authentication import Authentication

from .models import *
from.serializers import *

# Create your views here.
# @authentication_classes([Authentication])
@api_view(['POST'])
@permission_classes([IsAdminUser])
def gallery_post(request):

    caption = request.data['caption']
    thumbnail = request.data['thumbnail']
    description = request.data.get('description')
    GDSC_Gallery(caption=caption,thumbnail=thumbnail,description=description).save()
    return Response("OK")

@api_view(['GET'])
def gallery_get(request):
    db = GDSC_Gallery.objects.all()
    serializer = GallerySerializers(db,many=True)
    response = Response(serializer.data)
    # print(req.user)
    return response