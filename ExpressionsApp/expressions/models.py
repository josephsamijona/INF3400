from django.db import models
from django.contrib.auth.models import User

# Définition du modèle Expression pour stocker des expressions québécoises et leurs significations
class Expression(models.Model):
    # Champ pour l'expression, limité à 255 caractères, doit être unique dans la base de données
    expression = models.CharField(max_length=255, unique=True)
    # Champ pour la signification de l'expression, peut être de longueur arbitrairement longue
    meaning = models.TextField()

    # Méthode pour afficher une représentation string de l'objet, ici l'expression elle-même
    def __str__(self):
        return self.expression

# Définition du modèle Score pour enregistrer les scores des utilisateurs
class Score(models.Model):
    # Lien entre le score et un utilisateur, avec suppression en cascade si l'utilisateur est supprimé
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Champ pour le score, entier avec une valeur par défaut de 0
    score = models.IntegerField(default=0)

    # Méthode pour afficher une représentation string de l'objet, ici le nom d'utilisateur et son score
    def __str__(self):
        return f"{self.user.username}: {self.score}"

# Définition du modèle QuizQuestion pour stocker les questions du quiz et leurs réponses
class QuizQuestion(models.Model):
    # Champ pour la question, limité à 255 caractères
    question = models.CharField(max_length=255)
    # Champ pour la réponse correcte, stocké comme un booléen (True pour vrai, False pour faux)
    correct_answer = models.BooleanField()  # True pour vrai, False pour faux

    # Méthode pour afficher une représentation string de l'objet, ici la question du quiz
    def __str__(self):
        return self.question
