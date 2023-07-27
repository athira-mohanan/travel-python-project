from django.urls import path
from . import views

urlpatterns = [
    path('register',views.fun_registration,name='fun_registration'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]