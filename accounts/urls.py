from django.urls import path
from . import views

urlpatterns = [
    path('',views.allUsers),
    path('member/',views.members),
    path('admin/',views.admins),
    path('student/',views.students),
    path('register/',views.registerUser),
    path('login/',views.login),
    path('currentuser/',views.currentUser),

]