from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    CATEGORIE_CHOICES = [
        ('lieux', 'Lieux à visiter'),
        ('restaurants', 'Restaurants'),
    ]

    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ['-date_publication']

    def __str__(self):
        return self.titre 