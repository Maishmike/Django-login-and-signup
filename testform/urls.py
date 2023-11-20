from django.urls import path
from testform import views

app_name = 'testform'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home')
]
