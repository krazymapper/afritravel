from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'date_publication', 'auteur')
    list_filter = ('categorie', 'date_publication')
    search_fields = ('titre', 'contenu', 'adresse')
    date_hierarchy = 'date_publication'
    ordering = ('-date_publication',) 