from django.contrib import admin

from newsapp.models import Author, Category, Post, Comment, Subscription
from modeltranslation.admin import TranslationAdmin
# импортируем модель админки (вспоминаем модуль про переопределение стандартных админ-инструментов)


class AuthorAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице
    list_display = ['authorUser', 'authorRating']


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'categoryType', 'dateCreation', 'title', 'text', 'rating')
    list_filter = ('author', 'categoryType', 'dateCreation')
    search_fields = ('author', 'title')


class CommentAdmin(admin.ModelAdmin):
    # генерируем список имён всех полей
    list_display = [field.name for field in Comment._meta.get_fields()]


class CategoryTranslateAdmin(TranslationAdmin):
    model = Category


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryTranslateAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Subscription)
