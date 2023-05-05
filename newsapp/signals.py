from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from newsapp.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created_notify(instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        for category in categories:
            emails = User.objects.filter(
                subscriptions__category=category.pk
            ).values_list('email', flat=True)
            print(emails)
            subject = f'Новая публикация в категории {category}'

            text_content = (
                f'Автор: {instance.author}\n'
                f'Заголовок: {instance.title}\n\n'
                f'Ссылка на публикацию: http://127.0.0.1{instance.get_absolute_url()}'
            )
            html_content = (
                f'Автор: {instance.author}<br>'
                f'Заголовок: {instance.title}<br><br>'
                f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
                f'Ссылка на публикацию</a>'
            )
            for email in emails:
                msg = EmailMultiAlternatives(subject, text_content, None, [email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
