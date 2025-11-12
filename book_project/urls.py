from .views import salom_beruvchi, mamlakat_qaysi, mamlakat_va_viloyat, mamlakat_viloyat_va_shahar, akademiya, hamma_kitoblar, kitob_detail

from django.urls import path

urlpatterns = [
    path('ber/',salom_beruvchi),
    path('mamlakat/',mamlakat_qaysi),
    path('mamlakat/viloyat/',mamlakat_va_viloyat),
    path('mamlakat/viloyat/shahar/',mamlakat_viloyat_va_shahar),
    path('mamlakat/viloyat/shahar/akademiya/',akademiya),
    path('kitoblar/', hamma_kitoblar),
    path('kitoblar/<int:pk>/', kitob_detail)
]
