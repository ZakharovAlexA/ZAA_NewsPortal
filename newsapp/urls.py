from django.urls import path

from newsapp.views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view()),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view()),
]

