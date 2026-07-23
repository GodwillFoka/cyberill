from django.shortcuts import render

# ===== Multilingual articles =====
ARTICLES = {
    'fr': [
        {
            'slug': 'bienvenue-cyberill',
            'title': 'Bienvenue sur CYBERILL — Sécuriser le numérique, transformer l\'avenir',
            'category': 'Cyber',
            'date': '01 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop',
            'content': """
CYBERILL est né d'une conviction : la cybersécurité et la transformation digitale doivent être accessibles à tous.

Mon objectif est simple — donner de la valeur à mes connaissances et compétences, aider les personnes autour de moi à mieux exprimer leur génie, et contribuer à un environnement numérique plus sûr pour tous.

## Pourquoi CYBERILL ?

Le monde numérique évolue à une vitesse vertigineuse. Chaque jour, des milliers de nouvelles menaces apparaissent. Mais en parallèle, des opportunités incroyables se créent.

### Domaines d'intervention
- **Cybersécurité** : Audit, conseil, sensibilisation, pentesting
- **Transformation digitale** : Accompagnement à la digitalisation des processus
- **Développement logiciel** : Applications sécurisées, audit de code
- **Formation** : Workshops et sessions interactives

## Prochains articles
Je prépare une série sur les bases de la cybersécurité, le pentesting éthique, et la conformité DSGVO.

Restez connecté ! 🚀
""",
        },
        {
            'slug': 'cybersecurite-pour-tous',
            'title': 'Pourquoi la cybersécurité est l\'affaire de tous',
            'category': 'Sensibilisation',
            'date': '10 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&h=400&fit=crop',
            'content': """
On entend souvent dire que la cybersécurité est réservée aux experts. C'est faux. Dans un monde hyperconnecté, la sécurité est l'affaire de chacun.

## Les chiffres clés
- **60%** des PME qui subissent une cyberattaque ferment dans les 6 mois
- **95%** des failles de sécurité sont dues à des erreurs humaines
- **4,45M$** : coût moyen d'une violation de données (IBM 2023)

## Les gestes essentiels
1. **Mots de passe forts** — utilisez un gestionnaire
2. **2FA** — activez la double authentification
3. **Mises à jour** — elles contiennent des correctifs critiques
4. **Sauvegardes** — règle 3-2-1
5. **Méfiez-vous des emails suspects** — phishing

La cybersécurité commence par la sensibilisation. CYBERILL est là pour vous accompagner.
""",
        },
        {
            'slug': 'de-dschang-a-berlin',
            'title': 'De Dschang à Berlin — Mon parcours dans la cybersécurité',
            'category': 'Parcours',
            'date': '15 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=400&fit=crop',
            'content': """
Mon parcours commence à l'Université de Dschang, au Cameroun, où j'ai obtenu mon B.Sc. en IT Engineering.

## De l'IT à la cybersécurité
Après mon Master 1 en Software Engineering & IA, j'ai travaillé comme IT Systems Manager, Cybersecurity Specialist, et IT Project Coordinator.

C'est en voyant les défis de sécurité auxquels les organisations faisaient face que j'ai choisi la cybersécurité.

## Pourquoi Berlin ?
Berlin est devenu mon port d'attache — au cœur de l'innovation européenne, où la cybersécurité est un enjeu national. Mes certifications :
- EC-Council C|CT
- Cisco Junior Cybersecurity Analyst
- ANSSI SecNumAcadémie
- CSI Linux Certified Investigator

De Dschang à Berlin, chaque étape m'a apporté des compétences uniques. CYBERILL est ma façon de donner en retour.
""",
        },
    ],
    'en': [
        {
            'slug': 'welcome-cyberill',
            'title': 'Welcome to CYBERILL — Securing digital, transforming the future',
            'category': 'Cyber',
            'date': 'July 1, 2026',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop',
            'content': """
CYBERILL was born from a conviction: cybersecurity and digital transformation must be accessible to everyone.

My goal is simple — to bring value through my knowledge and skills, help people around me express their genius, and contribute to a safer digital environment for all.

## Why CYBERILL?

The digital world is evolving at breakneck speed. Every day, thousands of new threats emerge. But at the same time, incredible opportunities arise.

### Areas of expertise
- **Cybersecurity** : Audit, consulting, awareness, pentesting
- **Digital Transformation** : Process digitalization support
- **Software Development** : Secure applications, code audit
- **Training** : Workshops and interactive sessions

## Coming soon
A series on cybersecurity basics, ethical pentesting, and GDPR compliance.

Stay tuned! 🚀
""",
        },
        {
            'slug': 'cybersecurity-for-all',
            'title': 'Why cybersecurity is everyone\'s business',
            'category': 'Awareness',
            'date': 'July 10, 2026',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&h=400&fit=crop',
            'content': """
Many think cybersecurity is only for experts. That's wrong. In a hyper-connected world, security is everyone's concern.

## Key figures
- **60%** of SMBs that suffer a cyberattack close within 6 months
- **95%** of security breaches are due to human error
- **$4.45M** : average cost of a data breach (IBM 2023)

## Essential practices
1. **Strong passwords** — use a password manager
2. **2FA** — enable two-factor authentication
3. **Updates** — they contain critical security patches
4. **Backups** — 3-2-1 rule
5. **Watch suspicious emails** — phishing awareness

Cybersecurity starts with awareness. CYBERILL is here to guide you.
""",
        },
        {
            'slug': 'from-dschang-to-berlin',
            'title': 'From Dschang to Berlin — My journey in cybersecurity',
            'category': 'Journey',
            'date': 'July 15, 2026',
            'image': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=400&fit=crop',
            'content': """
My journey began at the University of Dschang, Cameroon, where I earned my B.Sc. in IT Engineering.

## From IT to cybersecurity
After my M.Sc. in Software Engineering & AI, I worked as IT Systems Manager, Cybersecurity Specialist, and IT Project Coordinator.

Seeing the security challenges organizations faced, I chose cybersecurity as my path.

## Why Berlin?
Berlin became my home — at the heart of European innovation, where cybersecurity is a national priority. My certifications:
- EC-Council C|CT
- Cisco Junior Cybersecurity Analyst
- ANSSI SecNumAcadémie
- CSI Linux Certified Investigator

From Dschang to Berlin, every step brought unique skills. CYBERILL is my way of giving back.
""",
        },
    ],
    'de': [
        {
            'slug': 'willkommen-cyberill',
            'title': 'Willkommen bei CYBERILL — Digital sichern, Zukunft gestalten',
            'category': 'Cyber',
            'date': '1. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop',
            'content': """
CYBERILL entstand aus der Überzeugung: Cybersicherheit und digitale Transformation müssen für alle zugänglich sein.

Mein Ziel ist einfach — Mehrwert durch mein Wissen und meine Fähigkeiten zu schaffen, Menschen dabei zu helfen, ihr Potenzial zu entfalten, und zu einer sichereren digitalen Umgebung beizutragen.

## Warum CYBERILL?

Die digitale Welt entwickelt sich rasant. Täglich tauchen Tausende neuer Bedrohungen auf. Doch gleichzeitig entstehen unglaubliche Chancen.

### Fachbereiche
- **Cybersicherheit** : Audit, Beratung, Sensibilisierung, Pentesting
- **Digitale Transformation** : Begleitung bei der Digitalisierung
- **Softwareentwicklung** : Sichere Anwendungen, Code-Audit
- **Schulungen** : Workshops und interaktive Sessions

## Demnächst
Eine Serie zu den Grundlagen der Cybersicherheit, ethischem Pentesting und DSGVO-Compliance.

Bleiben Sie dran! 🚀
""",
        },
        {
            'slug': 'cybersicherheit-fuer-alle',
            'title': 'Warum Cybersicherheit alle angeht',
            'category': 'Sensibilisierung',
            'date': '10. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&h=400&fit=crop',
            'content': """
Viele denken, Cybersicherheit sei nur etwas für Experten. Das stimmt nicht. In einer hypervernetzten Welt geht Sicherheit alle an.

## Wichtige Zahlen
- **60%** der KMU, die einen Cyberangriff erleiden, schließen innerhalb von 6 Monaten
- **95%** der Sicherheitsverletzungen sind auf menschliches Versagen zurückzuführen
- **4,45 Mio. $** : Durchschnittskosten einer Datenschutzverletzung (IBM 2023)

## Wichtige Maßnahmen
1. **Starke Passwörter** — verwenden Sie einen Passwort-Manager
2. **2FA** — aktivieren Sie die Zwei-Faktor-Authentifizierung
3. **Updates** — sie enthalten kritische Sicherheitspatches
4. **Backups** — 3-2-1-Regel
5. **Vorsicht bei E-Mails** — Phishing erkennen

Cybersicherheit beginnt mit Bewusstsein. CYBERILL begleitet Sie dabei.
""",
        },
        {
            'slug': 'von-dschang-nach-berlin',
            'title': 'Von Dschang nach Berlin — Mein Weg in die Cybersicherheit',
            'category': 'Werdegang',
            'date': '15. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=400&fit=crop',
            'content': """
Mein Weg begann an der Universität von Dschang, Kamerun, wo ich meinen B.Sc. in IT Engineering erwarb.

## Von der IT zur Cybersicherheit
Nach meinem M.Sc. in Software Engineering & KI arbeitete ich als IT-Systemmanager, Cybersicherheitsspezialist und IT-Projektkoordinator.

Als ich die Sicherheitsherausforderungen von Organisationen sah, entschied ich mich für die Cybersicherheit.

## Warum Berlin?
Berlin wurde meine Heimat — im Herzen der europäischen Innovation, wo Cybersicherheit eine nationale Priorität ist. Meine Zertifizierungen:
- EC-Council C|CT
- Cisco Junior Cybersecurity Analyst
- ANSSI SecNumAcadémie
- CSI Linux Certified Investigator

Von Dschang nach Berlin — jeder Schritt brachte einzigartige Erfahrungen. CYBERILL ist meine Art, etwas zurückzugeben.
""",
        },
    ],
}

def blog_list(request):
    lang = request.GET.get('lang', 'fr')
    # Get language from URL prefix via session
    from django.utils import translation
    lang = translation.get_language()
    articles = ARTICLES.get(lang, ARTICLES['fr'])
    return render(request, 'blog/list.html', {'articles': articles})

def blog_detail(request, slug):
    from django.utils import translation
    from django.http import Http404
    lang = translation.get_language()
    articles = ARTICLES.get(lang, ARTICLES['fr'])
    # Also try other languages if slug not found in current language
    article = None
    for a in articles:
        if a['slug'] == slug:
            article = a
            break
    if not article:
        # Fallback: check all languages
        for lang_code, arts in ARTICLES.items():
            for a in arts:
                if a['slug'] == slug:
                    article = a
                    break
            if article:
                break
    if not article:
        raise Http404("Article not found")
    return render(request, 'blog/detail.html', {'article': article})
