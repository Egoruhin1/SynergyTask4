from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('rent/<int:book_id>/', views.rent_book, name='rent_book'),
    path('add/', views.add_book, name='add_book'),
    path('my_rentals/', views.my_rentals, name='my_rentals'),
    path('register/', views.register, name='register'),
]
