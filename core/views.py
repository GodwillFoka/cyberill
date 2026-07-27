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
    html = """<table cellpadding="0" cellspacing="0" style="font-family: 'Inter', 'Segoe UI', Arial, sans-serif; font-size: 14px; color: #1A1A2E; max-width: 500px;">
  <tr>
    <td style="padding: 0 0 12px 0; border-bottom: 3px solid #E6681B;">
      <table cellpadding="0" cellspacing="0" width="100%">
        <tr>
          <td style="width: 70px; vertical-align: middle;">
            <!-- CYBERILL Shield Icon -->
            <table cellpadding="0" cellspacing="0" style="width: 56px; height: 56px; background: #20155C; border-radius: 50%;">
              <tr>
                <td style="text-align: center; color: #fff; font-size: 24px; font-weight: 900;">C</td>
              </tr>
            </table>
          </td>
          <td style="vertical-align: middle;">
            <div style="font-size: 20px; font-weight: 900; color: #20155C; letter-spacing: -0.5px;">Godwill FOKA</div>
            <div style="font-size: 12px; font-weight: 600; color: #E6681B; margin: 2px 0;">Cybersecurity Engineer · IT-Sicherheitsspezialist</div>
            <div style="font-size: 11px; color: #6B7280;">Initiator @ <span style="color: #20155C; font-weight: 700;">CYBERILL</span></div>
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td style="padding: 12px 0 0 0;">
      <table cellpadding="0" cellspacing="0" width="100%">
        <tr>
          <td style="padding: 4px 0;">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td style="padding-right: 8px; vertical-align: middle;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="#EA4335"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </td>
                <td style="vertical-align: middle;">
                  <a href="mailto:fokagodwill@gmail.com" style="color: #6B7280; text-decoration: none; font-size: 12px;">fokagodwill@gmail.com</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding: 4px 0;">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td style="padding-right: 8px; vertical-align: middle;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="#0A66C2"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                </td>
                <td style="vertical-align: middle;">
                  <a href="https://linkedin.com/in/godwillfoka" style="color: #6B7280; text-decoration: none; font-size: 12px;">linkedin.com/in/godwillfoka</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding: 4px 0;">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td style="padding-right: 8px; vertical-align: middle;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="#333"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
                </td>
                <td style="vertical-align: middle;">
                  <a href="https://github.com/GodwillFoka" style="color: #6B7280; text-decoration: none; font-size: 12px;">github.com/GodwillFoka</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding: 4px 0;">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td style="padding-right: 8px; vertical-align: middle;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="#E6681B"><path d="M22.65 14.39L12 22.13 1.35 14.39a.84.84 0 01-.3-.94L4.88 3.33a.42.42 0 01.4-.28.42.42 0 01.4.28l2.37 7.28h7.9l2.37-7.28a.42.42 0 01.4-.28.42.42 0 01.4.28l3.83 10.12a.84.84 0 01-.3.94z"/></svg>
                </td>
                <td style="vertical-align: middle;">
                  <a href="https://gitlab.com/GodwillFoka" style="color: #6B7280; text-decoration: none; font-size: 12px;">gitlab.com/GodwillFoka</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding: 4px 0;">
            <table cellpadding="0" cellspacing="0">
              <tr>
                <td style="padding-right: 8px; vertical-align: middle;">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="#E6681B"><path d="M12 2C6.48 2 2 6.48 2 12c0 5.52 4.48 10 10 10s10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
                </td>
                <td style="vertical-align: middle;">
                  <a href="https://cyberill.onrender.com" style="color: #E6681B; text-decoration: none; font-size: 12px; font-weight: 600;">cyberill.onrender.com</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td style="padding: 12px 0 0 0; border-top: 1px solid #E5E7EB; padding-top: 10px; margin-top: 10px;">
      <div style="font-size: 11px; color: #9CA3AF; font-style: italic;">"Securing digital, transforming the future"</div>
    </td>
  </tr>
</table>"""
    return HttpResponse(html)

def brand_email_signature_outlook(request):
    from django.http import HttpResponse
    import os
    from django.conf import settings
    path = os.path.join(settings.BASE_DIR, 'static', 'brand', 'email-signature-outlook.html')
    try:
        with open(path) as f:
            html = f.read()
    except:
        html = "Outlook signature not found"
    return HttpResponse(html)

# ===== Book Mode =====
def book_mode(request):
    from django.utils import translation
    lang = translation.get_language()
    return render(request, 'core/index-book.html', {'lang': lang})

# ===== Premium Home =====
def home_premium(request):
    from django.utils import translation
    lang = translation.get_language()
    return render(request, 'core/home-premium.html', {'lang': lang})

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
