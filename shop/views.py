from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import BookForm, RentalForm, UserRegistrationForm
from .models import Book, Category, Rental
from django.contrib.auth.decorators import login_required

def book_list(request):
    books = Book.objects.all()
    category = request.GET.get('category')
    author = request.GET.get('author')
    year = request.GET.get('year')

    if category:
        books = books.filter(category__name=category)
    if author:
        books = books.filter(author__icontains=author)
    if year:
        books = books.filter(year=year)

    categories = Category.objects.all()

    return render(request, 'shop/book_list.html', {'books': books, 'categories': categories})

@login_required
def rent_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.book = book
            rental.save()
            return redirect('book_list')
    else:
        form = RentalForm()

    return render(request, 'shop/rent_book.html', {'form': form, 'book': book})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'shop/add_book.html', {'form': form})

@login_required
def my_rentals(request):
    rentals = Rental.objects.filter(user=request.user)
    return render(request, 'shop/my_rentals.html', {'rentals': rentals})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'shop/register.html', {'form': form})
