from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render
from .forms import ContactForm


# Создаем контроллер главной страницы
def home_page(request: HttpRequest):
    return render(
        request,
        'info/home.html'
    )


# Создаем контроллер страницы контактов
def contact_page(request: HttpRequest):
    success_message = ''
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            success_message = f'''
                                Спасибо, <strong>{name}</strong>. 
                                Ваше сообщение получено
                            '''
            try:
                send_mail(
                    'Обратная связь',
                    success_message,
                    'admin@gvardy',
                    ['zeaglot@yandex.ru']
                )
            except:
                pass
    return render(
        request,
        'info/contact.html',
        {
            'form': form,
            'success_message': success_message,
        }
    )


# Создаем контроллер страницы о нас
def about_us_page(request: HttpRequest):
    return render(
        request,
        'info/about_us.html',
    )
