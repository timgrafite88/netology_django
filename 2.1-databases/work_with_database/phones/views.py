from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    # Получаем все телефоны из базы данных
    phones = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort == 'name':
        # Сортировка по названию в алфавитном порядке
        phones = phones.order_by('name')
    elif sort == 'min_price':
        # Сортировка по цене по возрастанию
        phones = phones.order_by('price')
    elif sort == 'max_price':
        # Сортировка по цене по убыванию
        phones = phones.order_by('-price')

    template = 'catalog.html'
    # Передаем список телефонов в контекст
    context = {'phones': phones, 'sort': sort}
    return render(request, template, context)

def show_product(request, slug):
    # Получаем телефон по slug (предполагается, что slug - это уникальное поле модели Phone)
    # Используем get_object_or_404 для обработки ошибок
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    # Передаем данные конкретного телефона в контекст
    context = {'phone': phone}
    return render(request, template, context)
