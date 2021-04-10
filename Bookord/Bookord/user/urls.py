from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('<str:username>/', views.profile_view, name='profile'),
]
