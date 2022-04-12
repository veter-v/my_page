from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from dataclasses import dataclass
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "Знак зодиака Скорпион",
    'sagittarius': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    'pisces': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
}

types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

zodiac_date = [
    [(1, 21), (2, 20), 'aquarius'],
    [(2, 20), (3, 21), 'pisces'],
    [(3, 21), (4, 21), 'aries'],
    [(4, 21), (5, 22), 'taurus'],
    [(5, 22), (6, 22), 'gemini'],
    [(6, 22), (7, 23), 'cancer'],
    [(7, 23), (8, 22), 'leo'],
    [(8, 22), (9, 24), 'virgo'],
    [(9, 24), (10, 24), 'libra'],
    [(10, 24), (11, 23), 'scorpio'],
    [(11, 23), (12, 23), 'sagittarius'],
    [(12, 23), (1, 21), 'capricorn'],
]


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):  # магический метод, который возвращает то, что мы хотим при обращении к классу
        return f'This is {self.name}'


# def leo(request):
#     return HttpResponse("Знак зодиака Лев<br>СРАТЬ<br>Я люблю тебя, милый")
#
#
# def scorpio(request):
#     return HttpResponse("Знак зодиака Скорпион")
#
#
# def aries(request):
#     return HttpResponse("Знак зодиака Овен<br>Лапа, ты овен!<br>Я люблю тебя!")
#
#
# def taurus(request):
#     return HttpResponse("Знак зодиака Телец")
#
#
# def gemini(request):
#     return HttpResponse("Знак зодиака Близнецы")
#
#
# def cancer(request):
#     return HttpResponse("Знак зодиака Рак")
#
#
# def virgo(request):
#     return HttpResponse("Знак зодиака Дева<br>Мой знак зодиака))")
#
#
# def libra(request):
#     return HttpResponse("Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).")
#  ........


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4х цифр - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    # f'<li><a href={redirect_path}>{sign.title()}</a></li>'
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    # response = render_to_string('horoscope/info_zodiac.html')
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
        'my_int': 234,
        'my_float': 324.544,
        'my_list': [1, 2],
        'my_tuple': (1, 2, 3, 4, 5, 6, 7, 8),
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_class': Person('Will', 55),
        'value': 0,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)  # заменяет render_to_string + HttpResponse


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def types(request):
    types_list = list(types_dict)
    rez = ''
    for type in types_list:
        redirect_path = reverse('a_type', args=[type])
        rez += f'<li><a href={redirect_path}>{type.upper()}</a></li>'
    response = f"""
    <ul>
    {rez}
    </ul>
    """
    return HttpResponse(response)


def atype(request, type: str):
    signs_intype = types_dict.get(type, None)
    if signs_intype:
        rez = ''
        for sign in signs_intype:
            redirect_path = reverse('horoscope-name', args=[sign])
            rez += f'<li><a href={redirect_path}>{sign.title()}</a></li>'
        response = f"""
        <ul>
        {rez}
        <ul>
        """
        return HttpResponse(response)


def get_info_by_date(request, month: int, day: int):
    if month < 13 and day <= 31:
        for date in zodiac_date:
            if (date[0][0] == month and date[0][1] <= day) or (date[1][0] == month and date[1][1] > day):
                return HttpResponseRedirect(reverse('horoscope-name', args=[date[2]]))
    else:
        return HttpResponseNotFound(f'<h2>Некорректно введена дата</h2><br>Месяц - {month}, день - {day}')

    # return HttpResponse("Знак зодиака Лев<br>СРАТЬ<br>Я люблю тебя, милый")
