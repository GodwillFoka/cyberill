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

# ===== Ressources Éducatives =====
def ressources(request):
    return render(request, 'core/ressources.html')

# ===== Cyber en chiffres =====
def stats_cyber(request):
    return render(request, 'core/stats.html')

# ===== CV =====
def cv_page(request):
    return render(request, 'core/cv.html')

# ===== Services =====
def services(request):
    return render(request, 'core/services.html')

def faq(request):
    return render(request, 'core/faq.html')

def google_verify(request):
    from django.http import HttpResponse
    return HttpResponse("google-site-verification: googlec4f4ea51a5ac0fa2.html", content_type="text/plain")

def brand_kit(request):
    return render(request, 'core/brand.html')

def brand_email_signature(request):
    from django.http import HttpResponse
    html = """<table cellpadding="0" cellspacing="0" style="font-family: Inter, Arial, sans-serif; font-size: 14px; color: #1A1A2E;">
  <tr>
    <td style="padding-right: 20px; vertical-align: top;">
      <div style="width: 80px; height: 80px; border-radius: 50%; background: #20155C; display: flex; align-items: center; justify-content: center; color: #fff; font-size: 32px; font-weight: 900;">GF</div>
    </td>
    <td style="vertical-align: top;">
      <div style="font-size: 18px; font-weight: 800; color: #20155C;">Godwill FOKA</div>
      <div style="font-size: 13px; font-weight: 600; color: #E6681B; margin: 2px 0;">Cybersecurity Engineer · IT-Sicherheitsspezialist</div>
      <div style="font-size: 12px; color: #6B7280; margin: 2px 0;">Initiator @ CYBERILL</div>
      <div style="margin-top: 8px; font-size: 12px; color: #6B7280;">
        📧 <a href="mailto:fokagodwill@gmail.com" style="color: #E6681B; text-decoration: none;">fokagodwill@gmail.com</a><br>
        🔗 <a href="https://linkedin.com/in/godwillfoka" style="color: #E6681B; text-decoration: none;">linkedin.com/in/godwillfoka</a><br>
        🌐 <a href="https://cyberill.onrender.com" style="color: #E6681B; text-decoration: none;">cyberill.onrender.com</a>
      </div>
      <div style="margin-top: 10px; padding-top: 10px; border-top: 2px solid #E6681B; font-size: 11px; color: #9CA3AF;">
        "Securing digital, transforming the future"
      </div>
    </td>
  </tr>
</table>"""
    return HttpResponse(html)

# ===== 404 personnalisée =====
def custom_404(request, exception=None):
    from django.utils import translation
    lang = translation.get_language()
    return render(request, '404.html', {'lang': lang}, status=404)

# ===== CV PDF Download =====
def cv_download(request):
    from django.http import HttpResponse
    from django.template.loader import render_to_string
    try:
        from xhtml2pdf import pisa
        html_string = render_to_string('core/cv_pdf.html')
        result = HttpResponse(content_type='application/pdf')
        result['Content-Disposition'] = 'attachment; filename="CV_Godwill_FOKA.pdf"'
        pisa_status = pisa.CreatePDF(html_string, dest=result)
        if pisa_status.err:
            raise Exception("PDF generation failed")
        return result
    except Exception as e:
        # Fallback: return HTML version
        html_string = render_to_string('core/cv_pdf.html')
        return HttpResponse(html_string, content_type='text/html')

# ===== Portfolio =====
def portfolio(request):
    import json
    from django.utils import translation
    lang = translation.get_language()
    
    repos = []
    try:
        import urllib.request
        r = urllib.request.urlopen(
            'https://api.github.com/users/GodwillFoka/repos?per_page=30&sort=updated',
            timeout=10
        )
        data = json.loads(r.read().decode())
        for repo in data:
            if not repo.get('fork', True) and 'bnd' not in repo['name'].lower():
                repos.append({
                    'name': repo['name'],
                    'description': repo['description'] or 'No description',
                    'url': repo['html_url'],
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'language': repo['language'] or '',
                    'updated': repo['updated_at'][:10],
                })
    except Exception:
        pass
    
    # Fallback: all known non-fork repos
    if not repos:
        repos = [
            {'name': 'cyberill', 'description': 'CYBERILL website — Django 5, Bootstrap 5, multilingual FR/EN/DE', 'url': 'https://github.com/GodwillFoka/cyberill', 'stars': 0, 'forks': 0, 'language': 'HTML', 'updated': '2026-07-23'},
            {'name': 'afrosec', 'description': 'AfroSec community platform', 'url': 'https://github.com/GodwillFoka/afrosec', 'stars': 0, 'forks': 0, 'language': 'HTML', 'updated': '2026-07-19'},
            {'name': 'Institut-Die-Suchenden_Website', 'description': 'Institutional website — IT solutions', 'url': 'https://github.com/GodwillFoka/Institut-Die-Suchenden_Website', 'stars': 0, 'forks': 0, 'language': 'HTML', 'updated': '2023-02-03'},
            {'name': 'Admin-Suchenden', 'description': 'Admin panel — management system', 'url': 'https://github.com/GodwillFoka/Admin-Suchenden', 'stars': 0, 'forks': 0, 'language': 'JavaScript', 'updated': '2023-01-04'},
            {'name': 'Women-Cyber-Go-Tour-2022', 'description': 'Women in Cyber event platform', 'url': 'https://github.com/GodwillFoka/Women-Cyber-Go-Tour-2022', 'stars': 0, 'forks': 0, 'language': 'PHP', 'updated': '2022-01-19'},
        ]
    
    return render(request, 'core/portfolio.html', {'repos': repos})
