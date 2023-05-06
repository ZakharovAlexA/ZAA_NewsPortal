from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from NewsPortal.settings import SITE_URL
from newsapp.models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created_notify(instance, **kwargs):
    # Функция реагирует на сигнал (post_add) записи в PostCategory, собирая всех подписчиков
    # и их email для отправки им уведомлений о новой публикации.

    if kwargs['action'] == 'post_add':
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
