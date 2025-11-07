from .views import Respublika , Mamlakat_viloyat , mamlakat_viloyat_shahar , mamlakat_viloyat_shahar_akademiya
from django.urls import path

urlpatterns = [
    path('mamlakat/' , Respublika) ,
    path('mamlakat/viloyat/', Mamlakat_viloyat) ,
    path('shahar/akademiya' , mamlakat_viloyat_shahar) ,
    path('akadamiya/', mamlakat_viloyat_shahar_akademiya)
]