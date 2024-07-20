from django.urls import path
from . import views  # Importation du module views du même package
from .views import quiz, main_menu, logout_view, about_view  # Importation spécifique de certaines vues

# Définition de la liste des motifs d'URLs pour l'application
urlpatterns = [
    # Route pour apprendre les expressions, pointe vers la vue 'learn_expressions'
    path('learn/', views.learn_expressions, name='learn_expressions'),
    
    # Route pour générer une phrase interrogative, pointe vers la vue 'generate_interrogative'
    path('interrogate/', views.generate_interrogative, name='generate_interrogative'),
    
    # Route pour afficher la signification d'une expression québécoise, pointe vers la vue 'display_meaning'
    path('meaning/', views.display_meaning, name='display_meaning'),
    
    # Route pour le quiz, utilise directement la vue 'quiz' importée
    path('quiz/', quiz, name='quiz'),
    
    # Route pour retourner au menu principal, utilise directement la vue 'main_menu' importée
    path('menu/', main_menu, name='main_menu'),
    
    # Route pour la déconnexion, utilise directement la vue 'logout_view' importée
    path('logout/', logout_view, name='logout_view'),
    
    # Route pour la page 'À propos', utilise directement la vue 'about_view' importée
    path('about/', about_view, name='about_view'),
]
