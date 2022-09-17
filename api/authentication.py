from rest_framework.authentication import BaseAuthentication
from accounts.models import User

class Authentication(BaseAuthentication):

    def authenticate(self, req):
        
        if 'Token' in req.headers:
            token = req.headers['Token']
        elif 'Token' in req.COOKIES:
            token = req.COOKIES['Token']
        else:
            return None
        
        try:
            user = User.objects.get(uid=token)
        except:
            return None
        return (user,None)        


         