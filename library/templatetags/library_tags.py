from django import template
import requests
from datetime import datetime
import locale

register = template.Library()

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

@register.simple_tag()
def get_time() -> str:
    data = requests.post('https://api.taxideli.ru/test/gettime').json()
    time = datetime.fromtimestamp(data['dataAns'] / 1000.0).strftime("%a, %d.%m.%Y %H:%M")
    return (time)