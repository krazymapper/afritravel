from django import forms
from .models import Article
from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    contenu = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Article
        fields = ['titre', 'categorie', 'adresse', 'latitude', 'longitude', 'image', 'contenu']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        } 