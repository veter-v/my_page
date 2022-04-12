from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')  # Какой класс и по какому названию регестрируем
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index),
    path('<my_date:sign_zodiac>/', views.get_my_date_converters),
    path('types/', views.types, name='zodiac-types'),
    path('types/<str:type>/', views.atype, name='a_type'),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views.get_my_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>/', views.get_info_by_date)
    # path('leo/', views.leo),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
    # path('gemini/', views.gemini),
    # path('cancer/', views.cancer),
    # path('virgo/', views.virgo),
    # path('libra/', views.libra),
    # path('scorpio/', views.scorpio),
    # path('sagittarius/', views.sagittarius),
    # path('capricorn/', views.capricorn),
    # path('aquarius/', views.aquarius),
    # path('pisces/', views.pisces),
]