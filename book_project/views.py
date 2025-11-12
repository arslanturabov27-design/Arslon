from django.shortcuts import render
from django.http import HttpResponse

from .models import BookModel

def salom_beruvchi(request):
    return HttpResponse("Asalomalekum ")

def mamlakat_qaysi(request):
    return HttpResponse("Ozbekiston Republikasi ")

def mamlakat_va_viloyat(request):
    return HttpResponse("Ozbekiston Respubklikasi Surxandaryo viloyati ")

def mamlakat_viloyat_va_shahar(request):
    return HttpResponse("Ozbekiston Respubklikasi Surxandaryo viloyati Termiz shahri ")

def akademiya(request):
    return HttpResponse("Surxandaryo viloyati Termiz shahri Joylinks akademiya ")


def hamma_kitoblar(request):
    all_books = BookModel.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'asosiy_sahifa.html', context)

def kitob_detail(request, pk):
    book = BookModel.objects.get(id=pk)
    context = {
        'book': book
    }
    return render(request, 'kitob_detail.html', context)