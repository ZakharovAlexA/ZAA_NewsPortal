"""NewsPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from newsapp.views import PostList, PostSearch, subscriptions

urlpatterns = [
    path('', cache_page(60)(PostList.as_view()), name='post_list'),
    path('search/', PostSearch.as_view(), name='search_posts'),
    path('admin/', admin.site.urls),
    path('news/', include('newsapp.urls_news')),
    path('articles/', include('newsapp.urls_articles')),
    path("accounts/", include("allauth.urls")),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
