from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', 'general')
        messages.success(
            request,
            _('Message envoyé avec succès')
        )
        return render(request, 'core/contact.html')
    return render(request, 'core/contact.html')

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        messages.success(
            request,
            f"Merci ! {email} — " + _("Message envoyé avec succès")
        )
    return redirect(request.META.get('HTTP_REFERER', '/'))

# ===== Ressources Éducatives =====
def ressources(request):
    return render(request, 'core/ressources.html')

# ===== Cyber en chiffres =====
def stats_cyber(request):
    return render(request, 'core/stats.html')

# ===== CV =====
def cv_page(request):
    return render(request, 'core/cv.html')

# ===== 404 personnalisée =====
def custom_404(request, exception=None):
    from django.utils import translation
    lang = translation.get_language()
    return render(request, '404.html', {'lang': lang}, status=404)

# ===== Portfolio =====
def portfolio(request):
    import json
    from django.utils import translation
    lang = translation.get_language()
    
    repos = []
    try:
        # Try using urllib (standard lib) instead of requests for Render compatibility
        import urllib.request
        r = urllib.request.urlopen(
            'https://api.github.com/users/GodwillFoka/repos?per_page=20&sort=updated',
            timeout=10
        )
        data = json.loads(r.read().decode())
        for repo in data:
            if not repo.get('fork', True):
                repos.append({
                    'name': repo['name'],
                    'description': repo['description'] or '',
                    'url': repo['html_url'],
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'language': repo['language'] or '',
                    'updated': repo['updated_at'][:10],
                })
    except Exception:
        pass
    
    # Fallback projects if API fails
    if not repos:
        repos = [
            {'name': 'cyberill', 'description': 'CYBERILL website — Django 5, Bootstrap 5', 'url': 'https://github.com/GodwillFoka/cyberill', 'stars': 0, 'forks': 0, 'language': 'Python', 'updated': '2026-07-23'},
            {'name': 'bnd-bewerbung', 'description': 'BND application dossier — LaTeX, XeLaTeX', 'url': 'https://github.com/GodwillFoka/bnd-bewerbung', 'stars': 0, 'forks': 0, 'language': 'TeX', 'updated': '2026-07-20'},
        ]
    
    return render(request, 'core/portfolio.html', {'repos': repos})
