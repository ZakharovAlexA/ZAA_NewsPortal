from django.urls import path
from newsapp.views import ArticlesCreate, ArticlesUpdate, ArticlesDelete

urlpatterns = [
    path('create/', ArticlesCreate.as_view(), name='create_articles'),
    path('<int:pk>/edit', ArticlesUpdate.as_view(), name='update_articles'),
    path('<int:pk>/delete', ArticlesDelete.as_view(), name='delete_articles'),
]
