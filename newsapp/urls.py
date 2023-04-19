from django.urls import path

from newsapp.views import PostList, PostDetail, PostSearch, PostCreate

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name='search_posts'),
    path('create/', PostCreate.as_view(), name='create_news'),
]

