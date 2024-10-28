from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    # Получаем все телефоны из базы данных
    phones = Phone.objects.all()
    template = 'catalog.html'
    # Передаем список телефонов в контекст
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    # Получаем телефон по slug (предполагается, что slug - это уникальное поле модели Phone)
    phone = get_object_or_404(Phone, slug=slug)  # Используем get_object_or_404 для обработки ошибок
    template = 'product.html'
    # Передаем данные конкретного телефона в контекст
    context = {'phone': phone}
    return render(request, template, context)