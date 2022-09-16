from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def allUsers(req):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def members(req):
    return Response('All members will be listed here')

@api_view(['GET'])
def students(req):
    return Response('All students will be listed here')

@api_view(['GET'])
def admins(req):
    return Response('All admins will be listed here')


@api_view(['GET','POST'])
def register(req):
    return Response('User Registration')


@api_view(['GET','POST'])
def login(req):
    return Response('User Registration')


@api_view(['GET'])
def isLoggedin(req):
    return Response('returns if user is logged in')



