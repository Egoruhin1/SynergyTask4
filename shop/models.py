from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Define a Category model to categorize books
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Define a Book model that contains information about books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

# Define a Rental model to track which users have rented which books
class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link the rental to a user
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Link the rental to a book
    rented_at = models.DateTimeField(auto_now_add=True)  # Record the time of rental
    return_due = models.DateTimeField()  # Record the due date for returning the book

    def __str__(self):
        return f"{self.book.title} rented by {self.user.username}"
