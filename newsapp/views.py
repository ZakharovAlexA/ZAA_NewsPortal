from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(categoryType='NW')


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
