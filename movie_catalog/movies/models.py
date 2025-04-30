from django.db import models

class Movie(models.Model):
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('drama', 'Drama'),
        ('sci-fi', 'Sci-Fi'),
        ('romance', 'Romance'),
        ('fantasy', 'Fantasy'),
        ('comedy', 'Comedy'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name
