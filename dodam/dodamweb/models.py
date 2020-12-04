from django.db import models

# Create your models here.


class book_info(models.Model):
    book_name = models.CharField(max_length=200)
    book_img = models.CharField(max_length=200)
    writer = models.CharField(max_length=10)
    short_intro = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.book_name


class in_book(models.Model):
    book_name = models.CharField(max_length=200)
    #book_name = models.ForeignKey(book_info, on_delete=models.CASCADE)
    full_intro = models.TextField()
    def __str__(self):
        return self.book_name


class music(models.Model):
    music_name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    mood = models.CharField(max_length=10)
    embedded_code = models.TextField()

