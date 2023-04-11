from django import template

register = template.Library()

# Словарь нецензурных слов.
WORDS_BLACK_LIST = {
    'редиска': 'р*****',
    'Редиска': 'Р*****',
}


@register.filter()
def censor(censored_text):
    """
    Фильтр применяется к тексту и заголовку для чистки от нецензурных слов
    :param censored_text: цензурируемый текст
    :return: возвращает очищенный текст
    """
    for black_list_key, black_list_value in WORDS_BLACK_LIST.items():
        censored_text = censored_text.replace(black_list_key, black_list_value)

    return censored_text
