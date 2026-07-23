from django.utils import translation

def site_language(request):
    """Ajoute la langue active et les URLs de navigation au contexte."""
    lang = translation.get_language()
    return {
        'lang': lang,
        'LANGUAGES': [
            ('fr', 'Français'),
            ('en', 'English'),
            ('de', 'Deutsch'),
        ],
        'current_path': request.path,
    }
