from django.urls import path,include
from . import views

urlpatterns = [
    path('post/',views.blogs_post),
    path('get/all/',views.blogs_get_all)
    
]