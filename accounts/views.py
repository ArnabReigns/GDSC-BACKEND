from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def allUsers(req):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def members(req):
    users = User.objects.filter(is_member__in=[True])
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def students(req):
    users = User.objects.filter(is_member__in=[False])
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def admins(req):
    users = User.objects.filter(is_admin__in=[True])
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def register(req):
    return Response('User Registration')


@api_view(['GET','POST'])
def login(req):
    return Response('User Registration')


@api_view(['GET'])
def isLoggedin(req):
    return Response('returns if user is logged in')



