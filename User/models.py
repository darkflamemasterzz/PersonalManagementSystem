from django.db import models
from Book.models import Book
from Movie.models import Movie

class User(models.Model):
    name = models.CharField(primary_key=True, max_length=50) # 主键
    eMail = models.EmailField(blank=True, max_length=254)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=50) # 主键
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default="")

class UserMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    isFinish = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default="")
