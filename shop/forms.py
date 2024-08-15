from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Rental

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'price', 'category']
        widgets = {
            'category': forms.Select()  # Это гарантирует, что будет отображаться выпадающий список
        }

class RentalForm(forms.ModelForm):
    return_due = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Rental
        fields = ['return_due']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

