from django.shortcuts import render

# Articles statiques — Phase 1 (pas de BDD)
ARTICLES = [
    {
        'slug': 'bienvenue-cyberill',
        'title': 'Bienvenue sur CYBERILL — Sécuriser le numérique, transformer l\'avenir',
        'category': 'Cyber',
        'date': '2026-07-01',
        'language': 'fr',
        'content': """
CYBERILL est né d'une conviction : la cybersécurité et la transformation digitale doivent être accessibles à tous.

Mon objectif est simple — donner de la valeur à mes connaissances et compétences, aider les personnes autour de moi à mieux exprimer leur génie, et contribuer à un environnement numérique plus sûr pour tous.

## Pourquoi CYBERILL ?

Le monde numérique évolue à une vitesse vertigineuse. Chaque jour, des milliers de nouvelles menaces apparaissent. Mais en parallèle, des opportunités incroyables se créent. CYBERILL est là pour t'aider à naviguer dans cet environnement complexe.

### Domaines d'intervention

- **Cybersécurité** : Audit, conseil, sensibilisation, pentesting
- **Transformation digitale** : Accompagnement à la digitalisation des processus
- **Formation** : Workshops et sessions de formation interactives
- **Community Management** : Animation de communautés tech et veille stratégique

## Prochains articles

Je prépare une série d'articles sur :
- Les bases de la cybersécurité pour les non-initiés
- Comment sécuriser son infrastructure IT
- Introduction au pentesting éthique
- La conformité DSGVO / ISO 27001 expliquée simplement

Restez connecté ! 🚀
""",
    },
    {
        'slug': 'cybersecurite-pour-tous',
        'title': 'Pourquoi la cybersécurité est l\'affaire de tous',
        'category': 'Sensibilisation',
        'date': '2026-07-10',
        'language': 'fr',
        'content': """
On entend souvent dire que la cybersécurité est un sujet réservé aux experts. C'est faux. Dans un monde où nos vies sont de plus en plus numériques, la sécurité est l'affaire de chacun.

## Les chiffres parlent d'eux-mêmes

- 60% des petites entreprises qui subissent une cyberattaque ferment dans les 6 mois
- 95% des failles de sécurité sont dues à des erreurs humaines
- Le coût moyen d'une violation de données est de 4,45 millions de dollars (IBM 2023)

## Les gestes simples qui changent tout

1. **Mots de passe forts** — utilisez un gestionnaire de mots de passe
2. **Double authentification (2FA)** — activez-la partout où c'est possible
3. **Mises à jour** — ne les reportez pas, elles contiennent des correctifs de sécurité
4. **Sauvegardes** — la règle 3-2-1 : 3 copies, 2 supports différents, 1 hors site
5. **Méfiez-vous des emails suspects** — ne cliquez pas sur les liens douteux

La cybersécurité commence par la sensibilisation. CYBERILL est là pour t'accompagner.
""",
    },
    {
        'slug': 'de-dschang-a-berlin',
        'title': 'De Dschang à Berlin — Mon parcours dans la cybersécurité',
        'category': 'Parcours',
        'date': '2026-07-15',
        'language': 'fr',
        'content': """
Mon parcours commence à l'Université de Dschang, au Cameroun, où j'ai obtenu mon B.Sc. en IT Engineering (Informatique fondamentale).

## De l'IT à la cybersécurité

Après mon Master 1 en Software Engineering & Intelligence Artificielle, j'ai travaillé comme :
- IT Systems Manager à l'Institut Die Suchenden
- IT & Cybersecurity Specialist chez ENIX SARL
- IT Project Coordinator chez VisibilityCAM

C'est en voyant les défis de sécurité auxquels les organisations étaient confrontées que j'ai décidé de me spécialiser en cybersécurité.

## Pourquoi Berlin ?

Berlin est devenu mon port d'attache — une ville au cœur de l'innovation européenne, où la cybersécurité est un enjeu national. Aujourd'hui, je continue ma spécialisation avec des certifications :
- EC-Council C|CT (Certified Cybersecurity Technician)
- Cisco Junior Cybersecurity Analyst
- ANSSI SecNumAcadémie
- CSI Linux Certified Investigator

De Dschang à Berlin, le chemin a été long mais chaque étape m'a apporté des compétences uniques. CYBERILL est ma façon de donner en retour.
""",
    },
]

def blog_list(request):
    return render(request, 'blog/list.html', {'articles': ARTICLES})

def blog_detail(request, slug):
    article = None
    for a in ARTICLES:
        if a['slug'] == slug:
            article = a
            break
    if not article:
        from django.http import Http404
        raise Http404("Article non trouvé")
    return render(request, 'blog/detail.html', {'article': article})
