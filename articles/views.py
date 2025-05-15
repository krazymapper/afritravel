from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Article
from .forms import ArticleForm
import json

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 9

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-date_publication')
        categorie = self.request.GET.get('categorie')
        search_query = self.request.GET.get('q')

        if categorie:
            queryset = queryset.filter(categorie=categorie)
        
        if search_query:
            queryset = queryset.filter(
                Q(titre__icontains=search_query) |
                Q(contenu__icontains=search_query)
            )

        return queryset

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class CarteView(TemplateView):
    template_name = 'articles/carte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
        markers = []
        for article in articles:
            markers.append({
                'id': article.id,
                'titre': article.titre,
                'categorie': article.get_categorie_display(),
                'latitude': float(article.latitude),
                'longitude': float(article.longitude),
                'adresse': article.adresse,
                'url': f'/article/{article.id}/',
                'image': article.image.url if article.image else None
            })
        context['markers'] = json.dumps(markers)
        return context

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('articles:article_list')

    def form_valid(self, form):
        form.instance.auteur = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('articles:article_list')

    def get_queryset(self):
        return Article.objects.filter(auteur=self.request.user)

def a_propos(request):
    return render(request, 'articles/a_propos.html') 