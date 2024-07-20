#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ExpressionsApp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Vérifier si l'argument 'runserver' est utilisé et si aucun port n'est spécifié
    if 'runserver' in sys.argv:
        # Trouver l'index de 'runserver' dans la liste des arguments
        index = sys.argv.index('runserver')
        # Vérifier si 'runserver' est le dernier argument ou si le prochain argument commence par '-'
        if len(sys.argv) <= index + 1 or sys.argv[index + 1].startswith('-'):
            # Ajouter le port 1500 par défaut
            sys.argv.insert(index + 1, '1500')

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
