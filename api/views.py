from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date, datetime,timedelta
# Create your views here.

@api_view(['GET'])
def home(req):
        return Response('Welcome To the API')


@api_view(['GET'])
def cookies(request):
    if request.method == 'GET':
        if 'bingo' in request.COOKIES:
            value = request.COOKIES['bingo']
            print(value)
            response = Response('Works')
            return response
        else:
            response = Response('Does Not Works')
            response.set_cookie('bingo', 'worked!',secure=True,httponly=True,samesite='none',expires=(datetime.now() + timedelta(days=10)))
            return response
