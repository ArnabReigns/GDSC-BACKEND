from django.urls import path,include
from . import views

urlpatterns = [
    path('post/',views.gallery_post),
    path('get/',views.gallery_get)
    
]