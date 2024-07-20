from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Expression, QuizQuestion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import random
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
 
# Vue pour apprendre les expressions, accessible uniquement aux utilisateurs connectés
@login_required
def learn_expressions(request):
    expressions = Expression.objects.all()  # Récupère toutes les expressions de la base de données
    return render(request, 'expressions/learn_expressions.html', {'expressions': expressions})

# Vue pour générer des phrases interrogatives, nécessite une authentification
@login_required
def generate_interrogative(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence')
        # Logique pour transformer la phrase ici (non implémentée dans ce commentaire)
        return render(request, 'expressions/result.html', {'result': sentence})
    return render(request, 'expressions/generate_interrogative.html')

# Vue pour afficher la signification d'expressions, répond avec JSON
@login_required
def display_meaning(request):
    if request.method == 'POST':
        expression = request.POST.get('expression')
        meaning = Expression.objects.filter(expression__iexact=expression).first()
        if meaning:
            return JsonResponse({'success': True, 'meaning': meaning.meaning})
        else:
            return JsonResponse({'success': False, 'error': 'Expression non trouvée'})
    return render(request, 'expressions/display_meaning.html')

# Vue pour un quiz, inclut une logique pour calculer le score basé sur les réponses correctes
@login_required
def quiz(request):
    if request.method == 'POST':
        responses = {int(key): (value == 'True') for key, value in request.POST.items() if key.isdigit()}
        score = sum(1 for question_id, user_answer in responses.items() if QuizQuestion.objects.get(id=question_id).correct_answer == user_answer)
        return JsonResponse({'score': score, 'total': len(responses)})
    else:
        questions = list(QuizQuestion.objects.all())
        random.shuffle(questions)
        questions = questions[:5]
        return render(request, 'expressions/quiz.html', {'questions': questions})
    
# Vue pour le menu principal, accessible uniquement aux utilisateurs connectés
@login_required   
def main_menu(request):
    return render(request, 'expressions/main_menu.html')

# Vue personnalisée pour le login utilisant la classe LoginView de Django
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('menu')

# Vue pour l'inscription utilisant une FormView pour gérer le formulaire d'inscription
class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)
 
# Vue pour déconnecter les utilisateurs
@login_required   
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

# Vue pour la page À propos, accessible uniquement aux utilisateurs connectés
@login_required
def about_view(request):
    return render(request, 'expressions/about_us.html')
