from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from api.authentication import Authentication
from django.contrib.auth.hashers import check_password

# Create your views here.


@api_view(['GET'])
@authentication_classes([Authentication])
@permission_classes([IsAuthenticated])
def allUsers(req):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    responce = Response(serializer.data)
    print(req.user)
    return responce


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



@api_view(['GET'])
def userDetails(req):
    return Response('Get User Details')

@api_view(['GET','POST'])
def registerUser(req):

    if req.method == 'POST':
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        else:
            return Response(serializer.errors)    
    else:
        return Response('Registration End Point')





@api_view(['GET','POST'])
def login(req):

    if req.method == 'POST':
        try:
            email = req.data['email']
            password = req.data['password']
        except:
            return Response('Credentials not provided')
        
        try:
            user = User.objects.get(email=email)
        except:
            return Response('Wrong email or password')
        
        if check_password(password,user.password):

            # looged in
            response =  Response({
                'status':'User Successfuly Logged In',
                'name':user.name,
                'email': user.email,
                'Authorisation Token' : user.uid
            })
            response.set_cookie('Token',user.uid, httponly=True, samesite='none',secure=True)
            return response
        else:
            return Response("Wrong email or password")
    else:

        return Response('User login endpoint')


@api_view(['GET'])
@authentication_classes([Authentication])
@permission_classes([IsAuthenticated])
def currentUser(req):
    user = req.user
    s = UserSerializer(user)
    return Response(s.data)
    




