from django.urls import path

from newsapp.views import PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('create/', PostCreate.as_view(), name='create_news'),
    path('<int:pk>/update', PostUpdate.as_view(), name='update_news'),
    path('<int:pk>/delete', PostDelete.as_view(), name='delete_news'),
]

