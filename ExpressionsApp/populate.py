import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExpressionsApp.settings')
django.setup()

from expressions.models import Expression

def add_expression(expression, meaning):
    expr, created = Expression.objects.get_or_create(expression=expression, meaning=meaning)
    if created:
        print(f'Added: {expression}')
    else:
        print(f'Exists: {expression}')

def populate():
    expressions_data = [
        ("Aller aux vues", "Aller au cinéma"),
        ("Au plus sacrant", "Au plus vite"),
        ("Avoir de la misère", "Avoir de la difficulté"),
        ("Avoir de l'eau dans la cave", "Avoir les pantalons trop courts"),
        ("Avoir du cœur au ventre", "Être vaillant"),
        ("Avoir du guts", "Avoir du cran, du courage"),
        ("Avoir du pain sur la planche", "Avoir beaucoup de travail"),
        ("Avoir la guedille au nez", "Avoir la morve au nez"),
        ("Avoir la journée dans le corps", "Être fourbu après une journée éreintante"),
        ("Avoir la tête enflée", "Être vaniteux, prétentieux"),
        ("Avoir le cœur gros", "Être triste"),
        ("Avoir le feu au cul", "Être très en colère ou être très pressé, fuir"),
        ("Avoir le motton", "Avoir la gorge serrée par l’émotion"),
        ("Avoir les baguettes en l'air", "Gesticuler beaucoup par emportement, par nervosité"),
        ("Avoir les mains plein de pouces", "Être malhabile de ses mains"),
        ("Avoir les deux yeux dans le même trou", "Être mal réveillé"),
        ("Avoir l'estomac dans les talons", "Avoir très faim"),
        ("Avoir mal au cœur", "Avoir envie de vomir"),
        ("Avoir une bad luck", "Être malchanceux"),
        ("Avoir une crotte sur le cœur", "Avoir du ressentiment"),
        ("Boss de bécosse", "Personne qui fait preuve d’une autorité prétentieuse malgré sa position hiérarchique modeste, petit chef"),
        ("Botcher son travail", "Faire un travail avec négligence"),
        ("C’est tiguidou", "C’est très bien"),
        ("Ça regarde mal", "Se présente ou s’annonce mal"),
        ("Ça va mal à shop", "Ça va très mal"),
        ("Ne vaut pas de la chnoute", "Ne vaut pas grand chose"),
        ("C'est de valeur", "C'est regrettable"),
        ("C'est le fun", "C'est amusant"),
        ("C'est pas vargeux", "Ne pas être extraordinaire, ne pas être terrible, être moche, médiocre"),
        ("C'est plate icitte", "C'est ennuyant ici"),
        ("C'est tout un numéro", "Personne originale"),
        ("C'est un visage à deux faces", "Hypocrite"),
        ("Virer son capot de bord", "Changer d'opinion"),
        ("Chanter la pomme", "Faire la cour"),
        ("Chic and swell", "Être chic"),
        ("Coûter un bras", "Coûter très cher"),
        ("C’est une autre paire de manches", "C’est complètement différent à cause d’une plus grande difficulté"),
        ("De seconde main", "Usagé"),
        ("Donner un lift", "Fait d’être transporté gratuitement dans un véhicule"),
        ("Dur de comprenure", "Difficile à comprendre"),
        ("En titi", "Beaucoup"),
        ("Être à côté de la track", "Être dans l'erreur"),
        ("Être aux oiseaux", "Être heureux"),
        ("Être dans de beaux draps", "Être dans une situation inconfortable, embarrassante"),
        ("Être de bonne heure sur le piton", "Être levé tôt"),
        ("Être en mosus", "Être en colère"),
        ("Être gras dur", "Comblé, fin prêt, chanceux"),
        ("Être gratteux", "Personne avare"),
        ("Être mouillé jusqu'aux os", "Être complètement trempé"),
        ("Être open", "Ouvert, avoir l'esprit ouvert"),
        ("Être ratoureux", "Être rusé et sournois"),
        ("Être sur son trente-six", "Être habillé chic"),
        ("Être tiré à quatre épingles", "Vêtu avec un soin minutieux"),
        ("Être willing", "Être prêt, être partant"),
        ("Fais de l'air!", "Déguerpis!"),
        ("Faire dur", "Avoir une apparence déplaisante, misérable ou ridicule"),
        ("Faire la baboune", "Faire la moue, bouder"),
        ("Faire la grasse matinée", "Se lever très tard, rester paresseusement au lit"),
        ("Tourner les coins ronds", "Expliquer qqch., procéder à qqch. de façon grossière, en sautant les points secondaires"),
        ("Faire un bon deal", "Faire une bonne affaire"),
        ("Fucker le chien", "Ne rien faire, faire des choses inutiles"),
        ("Déployer des efforts inutiles", "avoir du mal à faire quelque chose"),
        ("Fou comme un balai", "Très excité parce qu’on est très content d’apprendre quelque chose"),
        ("Frapper un nœud", "Subir un échec"),
        ("Frisé comme un mouton", "Très frisé"),
        ("Avoir frette", "Avoir très froid"),
        ("Grimper dans les rideaux", "Être agité, s’énerver, s’emporter"),
        ("J’ai mon voyage!", "Phrase exclamative servant à exprimer l’étonnement, la surprise, l’incrédulité"),
        ("En avoir son voyage", "Être exaspéré"),
        ("La levée du corps est raide", "Le réveil est difficile"),
        ("Lâcher son fou", "Donner libre cours à son envie de bouger, de s’amuser"),
        ("Lâcher un ouac", "Crier de peur ou de surprise"),
        ("L'affaire est dans le sac", "L’affaire est pratiquement réglée, le succès de l’entreprise est assuré"),
        ("Être en pieds de bas", "Être en chaussettes, sans chaussures"),
        ("Mets-en!", "Tu l’as dit!"),
        ("Mettre sa main au feu", "En être sûr au point d’en jurer"),
        ("Mettre ses culottes", "Prendre l’initiative, Réagir en prenant ses responsabilités"),
        ("Mouiller à boire debout", "Pleuvoir à verse, à seaux, à torrents, à flots"),
        ("Sans queue ni tête", "Dénué de sens"),
        ("S’ouvrir la trappe", "Parler alors que ce n’est pas le moment"),
        ("Pantoute", "Du tout"),
        ("Parler à travers son chapeau", "Parler à tort et à travers"),
        ("Partir pour la famille", "Tomber enceinte"),
        ("Passer la nuit sur la corde à linge", "Rester debout toute la nuit"),
        ("Péter de la broue", "Se vanter"),
        ("Péter le feu", "Avoir beaucoup d'énergie"),
        ("Pogner les nerfs", "S’énerver"),
        ("Prendre le champ", "Sortir de la route parce qu’on a perdu la maîtrise du véhicule"),
        ("Prendre le mors aux dents", "S’emporter"),
        ("Prendre une brosse", "Se rendre ivre"),
        ("Prendre ça mollo", "Prendre relaxe, doucement"),
        ("Rêver en couleurs", "Se faire des illusions"),
        ("Rire jaune", "Se forcer à rire, en dissimulant mal son dépit ou sa gêne"),
        ("Rouge comme une tomate", "Être très rouge en raison d’une émotion intense"),
        ("Sacrer patience", "Laisser quelqu’un tranquille"),
        ("Ne faire ni une ni deux", "Réagir très promptement"),
        ("Se faire griller la couenne", "Se faire bronzer"),
        ("Se faire laver", "Se faire dépouiller de tous ses biens"),
        ("Matcher", "Trouver un partenaire amoureux"),
        ("Se ronger les sangs", "Être très inquiet et impatient"),
        ("Se tirer une bûche", "S’approcher une chaise pour s’asseoir"),
        ("Têtu comme une mule", "Très têtu"),
        ("Tenir ça mort", "Ne pas en parler"),
        ("Tomber dans le panneau", "Tomber dans le piège"),
        ("Tourner autour du pot", "Perdre son temps en n’allant pas droit au but"),
        ("Être slaqué", "Être congédié"),
        ("Y aller aux toasts", "Aller vite"),
        ("Ne pas mener de train", "Ne pas faire de bruit"),
        ("Il ment comme il respire", "Il ment de façon spontanée et continuelle"),
        ("Y avoir du monde à la messe", "Y avoir foule"),
        ("Malcommode", "Qui est espiègle, turbulent, indiscipliné")
    ]

    for expression, meaning in expressions_data:
        add_expression(expression, meaning)

if __name__ == '__main__':
    populate()
