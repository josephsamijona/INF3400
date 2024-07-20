import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExpressionsApp.settings')
django.setup()


from expressions.models import QuizQuestion

def add_question(question_text, correct_answer):
    question, created = QuizQuestion.objects.get_or_create(
        question=question_text,
        defaults={'correct_answer': correct_answer}
    )
    if created:
        print(f'Added: {question_text}')
    else:
        print(f'Exists: {question_text}')

def populate():
    # Liste étendue de questions et réponses pour le quiz
    questions_and_answers = [
        ("Y aller aux toasts veut dire aller vite", True),
        ("C’est tiguidou veut dire Ne vaut pas grand-chose", False),  # La bonne réponse est "C'est très bien"
        ("Avoir le motton signifie être en colère", False),  # La bonne réponse est "Avoir la gorge serrée par l'émotion"
        ("Faire la baboune signifie faire la fête", False),  # La bonne réponse est "Bouder"
        ("Être gratteux signifie être généreux", False),  # La bonne réponse est "Être avare"
        # Ajout de 10 nouvelles questions
        ("'Avoir de l'eau dans la cave' signifie être dans une situation difficile", False),  # La bonne réponse est "Avoir les pantalons trop courts"
        ("'Être aux oiseaux' signifie être confus", False),  # La bonne réponse est "Être heureux"
        ("'Passer la nuit sur la corde à linge' signifie dormir à l'extérieur", False),  # La bonne réponse est "Rester debout toute la nuit"
        ("'Virer son capot de bord' signifie changer de voiture", False),  # La bonne réponse est "Changer d'opinion"
        ("'Se faire griller la couenne' signifie se faire bronzer", True),
        ("'Manger ses bas' signifie être très nerveux", True),
        ("'Tirer le diable par la queue' signifie avoir des difficultés financières", True),
        ("'Avoir la langue à terre' signifie être extrêmement fatigué", True),
        ("'Jouer du coude' signifie consommer beaucoup d'alcool", True),
        ("'Attacher ses patins' signifie se préparer à partir", False)  # La bonne réponse est "Se préparer à travailler dur"
    ]

    for question_text, correct_answer in questions_and_answers:
        add_question(question_text, correct_answer)

if __name__ == '__main__':
    populate()
