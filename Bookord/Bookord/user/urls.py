from django.urls import path
from . import views

urlpatterns=[
    path('', views.index_view, name='index'),
    path('<str:username>/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]