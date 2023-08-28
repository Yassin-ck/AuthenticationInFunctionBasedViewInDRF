from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.StudentApi,name='studentapi'),
    path('<int:pk>/',views.StudentApi,name='students'),
    path('auth/',include('rest_framework.urls'),name='auth')
]