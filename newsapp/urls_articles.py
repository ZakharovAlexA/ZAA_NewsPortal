from django.urls import path
from newsapp.views import ArticlesCreate

urlpatterns = [
    path('create/', ArticlesCreate.as_view(), name='create_articles'),
]
