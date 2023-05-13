from datetime import datetime, timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPortal.settings import SITE_URL, DEFAULT_FROM_EMAIL
from newsapp.models import Post


@shared_task
def task_create_notify(post_id):
    instance = Post.objects.get(id=post_id)
    categories = instance.postCategory.all()
    for category in categories:
        emails = User.objects.filter(
            subscriptions__category=category.pk
        ).values_list('email', flat=True)
        subject = f'Новая публикация в категории {category}'

        text_content = (
            f'Автор: {instance.author}\n'
            f'Заголовок: {instance.title}\n'
            f'{instance.preview}\n\n'
            f'Ссылка на публикацию: {SITE_URL}{instance.get_absolute_url()}'
        )
        html_content = (
            f'Автор: {instance.author}<br>'
            f'Заголовок: {instance.title}<br><br>'
            f'{instance.preview}\n\n'
            f'<a href="{SITE_URL}{instance.get_absolute_url()}">'
            f'Ссылка на публикацию</a>'
        )
        for email in emails:
            msg = EmailMultiAlternatives(subject, text_content, None, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()


@shared_task
def task_weekly_notify():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__pk', flat=True))
    subscribers = set(User.objects.filter(subscriptions__category__in=categories).values_list('email', flat=True))
    html_content = render_to_string(
        'weekly_posts.html',
        {
            'link': SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
