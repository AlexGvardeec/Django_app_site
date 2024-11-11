from django.contrib import admin
from .models import Article

# Регистрируем класс Article в меню админа
admin.site.register(Article)