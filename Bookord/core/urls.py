from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('<str:username>/<int:book_id>/', views.index_view, name='index'),
    path('<str:username>/<int:book_id>/aphorism/', views.aphorism_view, name='aphorism'),
    path('<str:username>/<int:book_id>/language/', views.language_view, name='language'),
    path('<str:username>/<int:book_id>/review/', views.review_view, name='review'),
    path('<str:username>/new/', views.newbook_view, name='newbook')
]
