from django.contrib import admin
from .models import Category, Book, Rental

# Регистрация модели Category в админке
admin.site.register(Category)

# Регистрация модели Rental в админке
admin.site.register(Rental)

# Используем декоратор для регистрации модели Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'price', 'category')  # Поля для отображения в списке
    fields = ('title', 'author', 'year', 'price', 'category')        # Поля для формы добавления/редактирования
