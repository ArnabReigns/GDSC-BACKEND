from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('cookie/',views.cookies),
    path('cookie/',views.cookies),
    path('accounts/',include('accounts.urls'))
]