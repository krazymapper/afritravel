import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import ArticleForm
from .models import Article
from .sanitize import clean_html

XSS_TITRE = '</script><script>alert("titre")</script>'


class SanitizeTests(TestCase):
    def test_supprime_scripts_et_gestionnaires(self):
        sale = '<p onclick="x()">Bonjour</p><script>alert(1)</script><a href="javascript:alert(1)">lien</a>'
        propre = clean_html(sale)
        self.assertNotIn("<script", propre)
        self.assertNotIn("onclick", propre)
        self.assertNotIn("javascript:", propre)
        self.assertIn("<p>Bonjour</p>", propre)

    def test_conserve_mise_en_forme_courante(self):
        html = '<h2>Ouidah</h2><p><strong>Route</strong> des esclaves</p><img src="https://exemple.org/a.jpg" alt="vue">'
        self.assertEqual(clean_html(html), html)

    def test_formulaire_nettoie_le_contenu(self):
        form = ArticleForm(data={
            "titre": "Abomey", "categorie": "lieux",
            "contenu": '<p>Palais</p><img src=x onerror="alert(1)">',
        })
        self.assertTrue(form.is_valid(), form.errors)
        self.assertNotIn("onerror", form.cleaned_data["contenu"])


class CarteTests(TestCase):
    def setUp(self):
        self.auteur = User.objects.create_user("abla", password="mot-de-passe-test")
        Article.objects.create(
            titre=XSS_TITRE, contenu="<p>x</p>", categorie="lieux", auteur=self.auteur,
            adresse="<img src=x onerror=alert(2)>", latitude="6.366700", longitude="2.433300",
        )

    def test_marqueurs_echappes_dans_json_script(self):
        rep = self.client.get(reverse("articles:carte"))
        self.assertEqual(rep.status_code, 200)
        html = rep.content.decode()
        self.assertNotIn(XSS_TITRE, html)  # jamais injecté brut
        self.assertIn('id="markers-data"', html)
        debut = html.index('id="markers-data" type="application/json">') + len('id="markers-data" type="application/json">')
        donnees = json.loads(html[debut:html.index("</script>", debut)])
        self.assertEqual(donnees[0]["titre"], XSS_TITRE)  # donnée intacte, simplement échappée
        self.assertEqual(donnees[0]["url"], reverse("articles:article_detail", args=[donnees[0]["id"]]))


class ListeTests(TestCase):
    def test_page_accueil(self):
        self.assertEqual(self.client.get(reverse("articles:article_list")).status_code, 200)
