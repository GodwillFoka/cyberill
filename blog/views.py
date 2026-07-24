from django.shortcuts import render

# ===== Multilingual articles =====
ARTICLES = {
    'fr': [
        # --- Article 1 ---
        {
            'slug': 'bienvenue-cyberill',
            'title': 'Bienvenue sur CYBERILL — Sécuriser le numérique, transformer l\'avenir',
            'category': 'Cyber',
            'date': '01 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop',
            'content': "CYBERILL est né d'une conviction : la cybersécurité et la transformation digitale doivent être accessibles à tous.\n\nMon objectif est simple — donner de la valeur à mes connaissances et compétences, aider les personnes autour de moi à mieux exprimer leur génie, et contribuer à un environnement numérique plus sûr pour tous.\n\n## Pourquoi CYBERILL ?\nLe monde numérique évolue à une vitesse vertigineuse. Chaque jour, des milliers de nouvelles menaces apparaissent.\n\n### Domaines\n- **Cybersécurité** : Audit, conseil, pentesting\n- **Transformation digitale** : Digitalisation\n- **Développement logiciel** : Apps sécurisées\n- **Formation** : Workshops\n\nRestez connecté ! 🚀",
        },
        # --- Article 2 ---
        {
            'slug': 'cybersecurite-pour-tous',
            'title': 'Pourquoi la cybersécurité est l\'affaire de tous',
            'category': 'Sensibilisation',
            'date': '10 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&h=400&fit=crop',
            'content': "On entend souvent dire que la cybersécurité est réservée aux experts. C'est faux.\n\n## Chiffres clés\n- **60%** des PME ferment après une cyberattaque\n- **95%** des failles dues à l'erreur humaine\n- **4,45M$** : coût moyen d'une violation (IBM 2023)\n\n## Gestes essentiels\n1. Mots de passe forts — utilisez un gestionnaire\n2. 2FA — activez la double authentification\n3. Mises à jour — correctifs critiques\n4. Sauvegardes — règle 3-2-1\n5. Méfiez-vous des emails suspects\n\nLa cybersécurité commence par la sensibilisation.",
        },
        # --- Article 3 ---
        {
            'slug': 'de-dschang-a-berlin',
            'title': 'De Dschang à Berlin — Mon parcours',
            'category': 'Parcours',
            'date': '15 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=400&fit=crop',
            'content': "Mon parcours commence à l'Université de Dschang, Cameroun.\n\n## De l'IT à la cybersécurité\nAprès mon Master 1 en Software Engineering & IA, j'ai travaillé comme IT Systems Manager, Cybersecurity Specialist, et IT Project Coordinator.\n\n## Pourquoi Berlin ?\nBerlin est au cœur de l'innovation européenne. Mes certifications : EC-Council C|CT, Cisco, ANSSI, CSI Linux.\n\nDe Dschang à Berlin — chaque étape m'a apporté des compétences uniques.",
        },
        # --- Article 4 : Pentesting ---
        {
            'slug': 'introduction-pentesting-ethique',
            'title': 'Introduction au Pentesting Éthique',
            'category': 'Pentesting',
            'date': '20 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=600&h=400&fit=crop',
            'content': "Le pentesting (test d'intrusion) est une simulation d'attaque cyber menée par des experts autorisés.\n\n## Les phases\n1. **Reconnaissance** — Collecte d'infos (OSINT, scanning)\n2. **Scanning** — Ports ouverts, services, vulnérabilités\n3. **Exploitation** — Accès via les failles identifiées\n4. **Maintien d'accès** — Persistance\n5. **Rapport** — Documentation et recommandations\n\n## Outils\n- **Nmap** : Scan de ports\n- **Metasploit** : Framework d'exploitation\n- **Burp Suite** : Test web\n- **Wireshark** : Analyse réseau\n\nLe pentesting éthique est essentiel pour corriger ses failles avant les attaquants.",
        },
        # --- Article 5 : OSINT ---
        {
            'slug': 'osint-collecte-information',
            'title': 'OSINT : L\'art de la collecte d\'information',
            'category': 'OSINT',
            'date': '25 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1560472355-536de3962603?w=600&h=400&fit=crop',
            'content': "L'OSINT (Open Source Intelligence) désigne la collecte et l'analyse d'informations provenant de sources publiques.\n\n## Sources\n- **Moteurs de recherche** : Google dorking, Shodan\n- **Réseaux sociaux** : LinkedIn, Twitter\n- **Whois** : Domaines\n- **GitHub** : Code source exposé\n- **Registres publics** : Entreprises\n\n## Applications\n- Reconnaissance pré-pentest\n- Investigations numériques\n- Sécurité offensive\n- Veille stratégique\n\nL'OSINT est la première étape d'une attaque — donc la première à sécuriser.",
        },
        # --- Article 6 : Forensics ---
        {
            'slug': 'digital-forensics-enquete',
            'title': 'Digital Forensics : Enquête numérique',
            'category': 'Forensics',
            'date': '30 juillet 2026',
            'image': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&h=400&fit=crop',
            'content': "La criminalistique numérique est la science de collecte, préservation et analyse de preuves électroniques.\n\n## Étapes clés\n1. **Préservation** — Copie forensique\n2. **Collecte** — Disques, RAM, logs\n3. **Analyse** — Fichiers supprimés, timeline\n4. **Rapport** — Chaîne de custody\n\n## Outils\n- **Autopsy / Sleuth Kit** : Analyse disque\n- **FTK Imager** : Acquisition\n- **Volatility** : Analyse RAM\n- **Wireshark** : Trafic réseau\n\nLa rigueur est la clé d'une enquête numérique réussie.",
        },
        # --- Article 7 : DSGVO ---
        {
            'slug': 'dsgvo-essentiel',
            'title': 'DSGVO : Ce qu\'il faut savoir',
            'category': 'Conformité',
            'date': '5 août 2026',
            'image': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=400&fit=crop',
            'content': "Le RGPD (DSGVO) est la réglementation européenne sur la protection des données personnelles.\n\n## Principes\n- Licéité, loyauté, transparence\n- Limitation des finalités\n- Minimisation des données\n- Exactitude\n- Limitation de conservation\n- Intégrité et confidentialité\n\n## Sanctions\nJusqu'à **20M€** ou **4% du CA mondial**.\n\n## Actions clés\n1. Registre des traitements\n2. Consentement explicite\n3. Chiffrement des données\n4. DPO si nécessaire\n5. Notification des violations sous 72h\n\nLa conformité DSGVO est un processus continu.",
        },
        # --- Article 8 : Linux ---
        {
            'slug': 'securiser-linux',
            'title': 'Sécuriser son infrastructure Linux',
            'category': 'Sécurité',
            'date': '10 août 2026',
            'image': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=400&fit=crop',
            'content': "Linux est réputé pour sa sécurité, mais une config par défaut ne suffit pas.\n\n## Hardening\n1. **Mises à jour** — apt update && apt upgrade\n2. **SSH** — Désactiver root, utiliser clés\n3. **Firewall** — iptables/ufw\n4. **SELinux / AppArmor** — Contrôle d'accès\n5. **Audit logs** — Fail2ban, auditd\n\n## Commandes\n```bash\nss -tuln  # ports ouverts\nfind / -perm -4000  # fichiers SUID\njournalctl -xe -n 50  # logs\n```\n\nUn serveur bien configuré est la base de toute infrastructure sécurisée.",
        },
        # --- Article 9 : Cloud Security ---
        {
            'slug': 'securite-cloud',
            'title': 'Sécurité Cloud : Protéger ses données dans le nuage',
            'category': 'Cloud',
            'date': '15 août 2026',
            'image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop',
            'content': "Le cloud computing transforme les entreprises, mais la sécurité reste clé.\n\n## Responsabilité partagée\nLe fournisseur sécurise l'infrastructure, vous sécurisez vos données.\n\n## Bonnes pratiques\n1. **IAM** — Moindre privilège\n2. **Chiffrement** — Au repos et en transit\n3. **Monitoring** — CloudTrail, GuardDuty\n4. **Backup** — Multi-régions\n5. **Security Groups** — Règles strictes\n\n## Pièges\n- Buckets S3 publics\n- Clés API exposées\n- Pas de MFA\n\nLe cloud est sécurisé… quand c'est bien configuré.",
        },
        # --- Article 10 : Social Engineering ---
        {
            'slug': 'ingenierie-sociale',
            'title': 'Ingénierie Sociale : La menace humaine',
            'category': 'Sensibilisation',
            'date': '20 août 2026',
            'image': 'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=600&h=400&fit=crop',
            'content': "L'art de manipuler les personnes pour obtenir des informations confidentielles.\n\n## Techniques\n1. **Phishing** — Emails frauduleux\n2. **Pretexting** — Faux scenario\n3. **Baiting** — Pièges physiques\n4. **Tailgating** — Accès non autorisé\n\n## Protection\n- Ne jamais divulguer d'infos sensibles\n- Vérifier l'identité\n- Former les équipes\n\nLa meilleure techno ne sert à rien si l'humain est la faille.",
        },
        # --- Article 11 : WiFi Security ---
        {
            'slug': 'securite-wifi',
            'title': 'Sécuriser son réseau WiFi',
            'category': 'Réseau',
            'date': '25 août 2026',
            'image': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&h=400&fit=crop',
            'content': "Le WiFi est une porte d'entrée prisée par les attaquants.\n\n## Bonnes pratiques\n1. Changer le mot de passe du routeur\n2. **WPA3** minimum\n3. Désactiver WPS\n4. SSID caché\n5. Filtrage MAC\n\n## Entreprise\n- Réseaux séparés (invités, IoT)\n- 802.1X + RADIUS\n- Guest network isolé\n\nUn WiFi bien configuré = première ligne de défense.",
        },
        # --- Article 12 : Python Cyber ---
        {
            'slug': 'python-cybersecurite',
            'title': 'Python pour la Cybersécurité',
            'category': 'Dev',
            'date': '30 août 2026',
            'image': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600&h=400&fit=crop',
            'content': "Python est le langage le plus utilisé en cybersécurité.\n\n## Bibliothèques\n- **Scapy** — Paquets réseau\n- **Requests** — HTTP\n- **Paramiko** — SSH\n- **Socket** — Réseau bas niveau\n\n## Cas d'usage\n- Analyse de logs\n- Automatisation de scans\n- Outils de force brute\n- Analyse de malware\n\nPython transforme des lignes de code en cyberpuissance.",
        },
        # --- Article 13 : Bug Bounty ---
        {
            'slug': 'bug-bounty-introduction',
            'title': 'Introduction au Bug Bounty',
            'category': 'Pentesting',
            'date': '5 septembre 2026',
            'image': 'https://images.unsplash.com/photo-1563206767-5b18f218e8de?w=600&h=400&fit=crop',
            'content': "Programme récompensant les chercheurs pour la découverte de vulnérabilités.\n\n## Plateformes\n- **HackerOne**\n- **Bugcrowd**\n- **Intigriti** (Europe)\n- **YesWeHack** (France)\n\n## Vulnérabilités courantes\n- XSS, SQLi, CSRF, IDOR, SSRF\n\n## Comment commencer\n1. Apprendre l'OWASP Top 10\n2. Compte HackerOne/Bugcrowd\n3. Programmes avec bonne réputation\n4. Documenter chaque trouvaille\n\nLe Bug Bounty = monter en compétences ET se faire payer !",
        },
    ],
    'en': [
        {
            'slug': 'welcome-cyberill',
            'title': 'Welcome to CYBERILL — Securing digital, transforming the future',
            'category': 'Cyber',
            'date': 'July 1, 2026',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop',
            'content': "CYBERILL was born from a conviction: cybersecurity and digital transformation must be accessible to everyone.\n\n## Why CYBERILL?\nThe digital world is evolving at breakneck speed.\n\n### Areas\n- **Cybersecurity** : Audit, consulting, pentesting\n- **Digital Transformation** : Process digitalization\n- **Software Development** : Secure apps\n- **Training** : Workshops\n\nStay tuned! 🚀",
        },
        {
            'slug': 'cybersecurity-for-all',
            'title': 'Why cybersecurity is everyone\'s business',
            'category': 'Awareness',
            'date': 'July 10, 2026',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&h=400&fit=crop',
            'content': "Many think cybersecurity is only for experts. That's wrong.\n\n## Key figures\n- **60%** of SMBs close after a cyberattack\n- **95%** of breaches due to human error\n- **$4.45M** : average breach cost (IBM 2023)\n\n## Essential practices\n1. Strong passwords\n2. 2FA\n3. Updates\n4. Backups — 3-2-1 rule\n5. Watch suspicious emails\n\nCybersecurity starts with awareness.",
        },
        {
            'slug': 'from-dschang-to-berlin',
            'title': 'From Dschang to Berlin — My journey',
            'category': 'Journey',
            'date': 'July 15, 2026',
            'image': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=400&fit=crop',
            'content': "My journey began at the University of Dschang, Cameroon.\n\n## From IT to cybersecurity\nAfter my M.Sc. in Software Engineering & AI, I worked as IT Systems Manager, Cybersecurity Specialist.\n\n## Why Berlin?\nBerlin became my home. My certifications: EC-Council C|CT, Cisco, ANSSI, CSI Linux.\n\nFrom Dschang to Berlin — every step brought unique skills.",
        },
        {
            'slug': 'introduction-ethical-pentesting',
            'title': 'Introduction to Ethical Pentesting',
            'category': 'Pentesting',
            'date': 'July 20, 2026',
            'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=600&h=400&fit=crop',
            'content': "Penetration testing is a simulated cyber attack conducted by authorized experts.\n\n## Phases\n1. **Reconnaissance** — Information gathering\n2. **Scanning** — Open ports, services\n3. **Exploitation** — Unauthorized access\n4. **Maintaining Access** — Persistence\n5. **Reporting** — Documentation\n\n## Tools\n- **Nmap**: Port scanning\n- **Metasploit**: Exploitation framework\n- **Burp Suite**: Web testing\n- **Wireshark**: Traffic analysis\n\nEthical pentesting helps find and fix vulnerabilities before attackers do.",
        },
        {
            'slug': 'osint-information-gathering',
            'title': 'OSINT: The Art of Information Gathering',
            'category': 'OSINT',
            'date': 'July 25, 2026',
            'image': 'https://images.unsplash.com/photo-1560472355-536de3962603?w=600&h=400&fit=crop',
            'content': "OSINT (Open Source Intelligence) refers to collecting information from public sources.\n\n## Sources\n- **Search Engines**: Google dorking, Shodan\n- **Social Media**: LinkedIn, Twitter\n- **Whois**: Domain info\n- **GitHub**: Exposed code\n- **Public Registries**: Companies\n\n## Applications\n- Pre-pentest reconnaissance\n- Digital investigations\n- Offensive security\n- Threat monitoring\n\nOSINT is often the first step of an attack — secure it first.",
        },
        {
            'slug': 'digital-forensics-investigation',
            'title': 'Digital Forensics: Cyber Investigation',
            'category': 'Forensics',
            'date': 'July 30, 2026',
            'image': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&h=400&fit=crop',
            'content': "Digital forensics is the science of collecting and analyzing electronic evidence.\n\n## Key Steps\n1. **Preservation** — Forensic copy\n2. **Collection** — Disks, RAM, logs\n3. **Analysis** — Deleted files, timeline\n4. **Reporting** — Chain of custody\n\n## Tools\n- **Autopsy / Sleuth Kit**: Disk analysis\n- **FTK Imager**: Acquisition\n- **Volatility**: RAM analysis\n- **Wireshark**: Network traffic\n\nRigor is key to a successful digital investigation.",
        },
        {
            'slug': 'gdpr-essentials',
            'title': 'GDPR: What You Need to Know',
            'category': 'Compliance',
            'date': 'August 5, 2026',
            'image': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=400&fit=crop',
            'content': "GDPR is the European regulation governing personal data processing.\n\n## Core Principles\n- Lawfulness, fairness, transparency\n- Purpose limitation\n- Data minimization\n- Accuracy\n- Storage limitation\n- Integrity and confidentiality\n\n## Penalties\nUp to **€20M** or **4% of global turnover**.\n\n## Key Actions\n1. Processing register\n2. Explicit consent\n3. Data encryption\n4. DPO appointment\n5. Breach notification within 72h\n\nGDPR compliance is a continuous process.",
        },
        {
            'slug': 'linux-security-hardening',
            'title': 'Securing Your Linux Infrastructure',
            'category': 'Security',
            'date': 'August 10, 2026',
            'image': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=400&fit=crop',
            'content': "Linux is renowned for security, but default configurations aren't enough.\n\n## Hardening\n1. **Updates** — apt update && apt upgrade\n2. **SSH** — Disable root, use keys\n3. **Firewall** — iptables/ufw\n4. **SELinux / AppArmor** — Access control\n5. **Log auditing** — Fail2ban\n\n## Commands\n```bash\nss -tuln\nfind / -perm -4000\njournalctl -xe -n 50\n```\n\nA well-configured server is the foundation of secure infrastructure.",
        },
        # --- Article 9 : Cloud Security ---
        {
            'slug': 'cloud-security',
            'title': 'Cloud Security: Protecting Your Data',
            'category': 'Cloud',
            'date': 'August 15, 2026',
            'image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop',
            'content': "Cloud computing transforms businesses, but security remains key.\n\n## Shared Responsibility\nThe provider secures infrastructure, you secure your data.\n\n## Best Practices\n1. **IAM** — Least privilege\n2. **Encryption** — At rest and in transit\n3. **Monitoring** — CloudTrail, GuardDuty\n4. **Backup** — Multi-region\n5. **Security Groups** — Strict rules\n\n## Common pitfalls\n- Public S3 buckets\n- Exposed API keys\n- No MFA\n\nThe cloud is secure… when properly configured.",
        },
        # --- Article 10 : Social Engineering ---
        {
            'slug': 'social-engineering',
            'title': 'Social Engineering: The Human Threat',
            'category': 'Awareness',
            'date': 'August 20, 2026',
            'image': 'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=600&h=400&fit=crop',
            'content': "Social engineering is the art of manipulating people to obtain confidential information.\n\n## Techniques\n1. **Phishing** — Fraudulent emails\n2. **Pretexting** — Fake scenario\n3. **Baiting** — Physical traps\n4. **Tailgating** — Unauthorized access\n\n## Protection\n- Never disclose sensitive info\n- Verify identity\n- Train your teams\n\nThe best tech is useless if humans are the weak link.",
        },
        # --- Article 11 : WiFi Security ---
        {
            'slug': 'wifi-security',
            'title': 'Securing Your WiFi Network',
            'category': 'Network',
            'date': 'August 25, 2026',
            'image': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&h=400&fit=crop',
            'content': "WiFi is a favorite entry point for attackers.\n\n## Best Practices\n1. Change router default password\n2. **WPA3** minimum\n3. Disable WPS\n4. Hide SSID\n5. MAC filtering\n\n## Enterprise\n- Separate networks (guests, IoT)\n- 802.1X + RADIUS\n- Isolated guest network\n\nGood WiFi = first line of defense.",
        },
        # --- Article 12 : Python Cyber ---
        {
            'slug': 'python-cybersecurity',
            'title': 'Python for Cybersecurity',
            'category': 'Dev',
            'date': 'August 30, 2026',
            'image': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600&h=400&fit=crop',
            'content': "Python is the most used language in cybersecurity.\n\n## Libraries\n- **Scapy** — Network packets\n- **Requests** — HTTP\n- **Paramiko** — SSH\n- **Socket** — Low-level network\n\n## Use cases\n- Log analysis\n- Scan automation\n- Brute force tools\n- Malware analysis\n\nPython turns code into cyberpower.",
        },
        # --- Article 13 : Bug Bounty ---
        {
            'slug': 'bug-bounty-intro',
            'title': 'Introduction to Bug Bounty',
            'category': 'Pentesting',
            'date': 'September 5, 2026',
            'image': 'https://images.unsplash.com/photo-1563206767-5b18f218e8de?w=600&h=400&fit=crop',
            'content': "Bug Bounty programs reward researchers for finding vulnerabilities.\n\n## Platforms\n- **HackerOne**\n- **Bugcrowd**\n- **Intigriti** (Europe)\n\n## Common vulns\n- XSS, SQLi, CSRF, IDOR, SSRF\n\n## Getting started\n1. Learn OWASP Top 10\n2. Create HackerOne/Bugcrowd account\n3. Target good reputation programs\n4. Document every finding\n\nBug Bounty = level up skills AND get paid!",
        },
    ],
    'de': [
        {
            'slug': 'willkommen-cyberill',
            'title': 'Willkommen bei CYBERILL — Digital sichern, Zukunft gestalten',
            'category': 'Cyber',
            'date': '1. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop',
            'content': "CYBERILL entstand aus der Überzeugung: Cybersicherheit und digitale Transformation müssen für alle zugänglich sein.\n\n## Warum CYBERILL?\nDie digitale Welt entwickelt sich rasant.\n\n### Bereiche\n- **Cybersicherheit** : Audit, Beratung, Pentesting\n- **Digitale Transformation** : Digitalisierung\n- **Softwareentwicklung** : Sichere Anwendungen\n- **Schulungen** : Workshops\n\nBleiben Sie dran! 🚀",
        },
        {
            'slug': 'cybersicherheit-fuer-alle',
            'title': 'Warum Cybersicherheit alle angeht',
            'category': 'Sensibilisierung',
            'date': '10. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&h=400&fit=crop',
            'content': "Viele denken, Cybersicherheit sei nur etwas für Experten. Das stimmt nicht.\n\n## Wichtige Zahlen\n- **60%** der KMU schließen nach einem Cyberangriff\n- **95%** der Verstöße durch menschliches Versagen\n- **4,45 Mio. $** : Durchschnittskosten (IBM 2023)\n\n## Wichtige Maßnahmen\n1. Starke Passwörter\n2. 2FA aktivieren\n3. Updates installieren\n4. Backups — 3-2-1-Regel\n5. Vorsicht bei E-Mails\n\nCybersicherheit beginnt mit Bewusstsein.",
        },
        {
            'slug': 'von-dschang-nach-berlin',
            'title': 'Von Dschang nach Berlin — Mein Weg',
            'category': 'Werdegang',
            'date': '15. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?w=600&h=400&fit=crop',
            'content': "Mein Weg begann an der Universität von Dschang, Kamerun.\n\n## Von der IT zur Cybersicherheit\nNach meinem M.Sc. in Software Engineering & KI arbeitete ich als IT-Systemmanager und Cybersicherheitsspezialist.\n\n## Warum Berlin?\nBerlin wurde meine Heimat. Meine Zertifizierungen: EC-Council C|CT, Cisco, ANSSI, CSI Linux.\n\nJeder Schritt brachte einzigartige Erfahrungen.",
        },
        {
            'slug': 'einfuhrung-ethisches-pentesting',
            'title': 'Einführung in ethisches Pentesting',
            'category': 'Pentesting',
            'date': '20. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=600&h=400&fit=crop',
            'content': "Pentesting ist eine simulierte Cyberattacke durch autorisierte Experten.\n\n## Phasen\n1. **Aufklärung** — Informationssammlung\n2. **Scanning** — Offene Ports, Dienste\n3. **Ausnutzung** — Unbefugter Zugriff\n4. **Zugriff halten** — Persistenz\n5. **Bericht** — Dokumentation\n\n## Werkzeuge\n- **Nmap**: Port-Scan\n- **Metasploit**: Exploitation-Framework\n- **Burp Suite**: Web-Testing\n- **Wireshark**: Netzwerkanalyse\n\nEthisches Pentesting findet Schwachstellen bevor Angreifer es tun.",
        },
        {
            'slug': 'osint-informationssammlung',
            'title': 'OSINT: Die Kunst der Informationssammlung',
            'category': 'OSINT',
            'date': '25. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1560472355-536de3962603?w=600&h=400&fit=crop',
            'content': "OSINT (Open Source Intelligence) bezeichnet die Sammlung von Informationen aus öffentlichen Quellen.\n\n## Quellen\n- **Suchmaschinen**: Google dorking, Shodan\n- **Soziale Medien**: LinkedIn, Twitter\n- **Whois**: Domain-Informationen\n- **GitHub**: Quellcode\n- **Öffentliche Register**: Unternehmen\n\n## Anwendungen\n- Pre-Pentest-Aufklärung\n- Digitale Ermittlungen\n- Offensive Sicherheit\n- Bedrohungsüberwachung\n\nOSINT ist oft der erste Schritt eines Angriffs.",
        },
        {
            'slug': 'digital-forensics-ermittlung',
            'title': 'Digital Forensics: Digitale Ermittlung',
            'category': 'Forensik',
            'date': '30. Juli 2026',
            'image': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&h=400&fit=crop',
            'content': "Digital Forensics ist die Wissenschaft der Sammlung und Analyse elektronischer Beweise.\n\n## Schritte\n1. **Sicherung** — Forensische Kopie\n2. **Sammlung** — Datenträger, RAM, Logs\n3. **Analyse** — Gelöschte Dateien, Timeline\n4. **Bericht** — Chain of Custody\n\n## Werkzeuge\n- **Autopsy / Sleuth Kit**: Festplattenanalyse\n- **FTK Imager**: Forensische Erfassung\n- **Volatility**: RAM-Analyse\n- **Wireshark**: Netzwerkverkehr\n\nGründlichkeit ist der Schlüssel zu erfolgreichen digitalen Ermittlungen.",
        },
        {
            'slug': 'dsgvo-grundlagen',
            'title': 'DSGVO: Was Sie wissen müssen',
            'category': 'Compliance',
            'date': '5. August 2026',
            'image': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=600&h=400&fit=crop',
            'content': "Die DSGVO ist die europäische Verordnung zum Schutz personenbezogener Daten.\n\n## Grundsätze\n- Rechtmäßigkeit, Transparenz\n- Zweckbindung\n- Datenminimierung\n- Richtigkeit\n- Speicherbegrenzung\n- Integrität und Vertraulichkeit\n\n## Strafen\nBis zu **20 Mio. €** oder **4% des weltweiten Umsatzes**.\n\n## Maßnahmen\n1. Verarbeitungsverzeichnis\n2. Ausdrückliche Einwilligung\n3. Datenverschlüsselung\n4. DSB-Bestellung\n5. Verletzungsmeldung in 72h\n\nDSGVO-Compliance ist ein kontinuierlicher Prozess.",
        },
        {
            'slug': 'linux-infrastruktur-sichern',
            'title': 'Linux-Infrastruktur sichern',
            'category': 'Sicherheit',
            'date': '10. August 2026',
            'image': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&h=400&fit=crop',
            'content': "Linux ist für Sicherheit bekannt, aber Standardkonfigurationen reichen nicht.\n\n## Härtung\n1. **Updates** — apt update && apt upgrade\n2. **SSH** — Root-Login deaktivieren, Schlüssel\n3. **Firewall** — iptables/ufw\n4. **SELinux / AppArmor** — Zugriffskontrolle\n5. **Log-Überwachung** — Fail2ban\n\n## Befehle\n```bash\nss -tuln\nfind / -perm -4000\njournalctl -xe -n 50\n```\n\nEin gut konfigurierter Server ist die Basis sicherer Infrastruktur.",
        },
        # --- Article 9 : Cloud Security ---
        {
            'slug': 'cloud-sicherheit',
            'title': 'Cloud-Sicherheit: Daten in der Cloud schützen',
            'category': 'Cloud',
            'date': '15. August 2026',
            'image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600&h=400&fit=crop',
            'content': "Cloud-Computing verändert Unternehmen, aber Sicherheit bleibt entscheidend.\n\n## Geteilte Verantwortung\nDer Anbieter sichert die Infrastruktur, Sie sichern Ihre Daten.\n\n## Best Practices\n1. **IAM** — Wenigste Rechte\n2. **Verschlüsselung** — Ruhend und in Transit\n3. **Monitoring** — CloudTrail, GuardDuty\n4. **Backup** — Multi-Region\n5. **Security Groups** — Strenge Regeln\n\n## Häufige Fallstricke\n- Öffentliche S3-Buckets\n- Exponierte API-Keys\n- Kein MFA\n\nDie Cloud ist sicher… wenn richtig konfiguriert.",
        },
        # --- Article 10 : Social Engineering ---
        {
            'slug': 'social-engineering-mensch',
            'title': 'Social Engineering: Die menschliche Bedrohung',
            'category': 'Sensibilisierung',
            'date': '20. August 2026',
            'image': 'https://images.unsplash.com/photo-1573164713714-d95e436ab8d6?w=600&h=400&fit=crop',
            'content': "Social Engineering ist die Kunst, Menschen zu manipulieren, um vertrauliche Informationen zu erhalten.\n\n## Techniken\n1. **Phishing** — Betrügerische E-Mails\n2. **Pretexting** — Falsches Szenario\n3. **Baiting** — Physische Fallen\n4. **Tailgating** — Unbefugter Zutritt\n\n## Schutz\n- Niemals sensible Infos preisgeben\n- Identität prüfen\n- Teams schulen\n\nBeste Technik nützt nichts, wenn der Mensch die Schwachstelle ist.",
        },
        # --- Article 11 : WiFi Security ---
        {
            'slug': 'wifi-sicherheit',
            'title': 'WLAN-Netzwerk sichern',
            'category': 'Netzwerk',
            'date': '25. August 2026',
            'image': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&h=400&fit=crop',
            'content': "WLAN ist ein beliebter Einstiegspunkt für Angreifer.\n\n## Best Practices\n1. Router-Standardpasswort ändern\n2. **WPA3** minimum\n3. WPS deaktivieren\n4. SSID verstecken\n5. MAC-Filter\n\n## Unternehmen\n- Getrennte Netzwerke (Gäste, IoT)\n- 802.1X + RADIUS\n- Gästenetzwerk isoliert\n\nGutes WLAN = erste Verteidigungslinie.",
        },
        # --- Article 12 : Python Cyber ---
        {
            'slug': 'python-cybersicherheit',
            'title': 'Python für Cybersicherheit',
            'category': 'Dev',
            'date': '30. August 2026',
            'image': 'https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=600&h=400&fit=crop',
            'content': "Python ist die meistgenutzte Sprache in der Cybersicherheit.\n\n## Bibliotheken\n- **Scapy** — Netzwerkpakete\n- **Requests** — HTTP\n- **Paramiko** — SSH\n- **Socket** — Niedriges Netzwerk\n\n## Anwendungsfälle\n- Log-Analyse\n- Scan-Automatisierung\n- Brute-Force-Tools\n- Malware-Analyse\n\nPython verwandelt Code in Cyberkraft.",
        },
        # --- Article 13 : Bug Bounty ---
        {
            'slug': 'bug-bounty-einfuhrung',
            'title': 'Einführung in Bug Bounty',
            'category': 'Pentesting',
            'date': '5. September 2026',
            'image': 'https://images.unsplash.com/photo-1563206767-5b18f218e8de?w=600&h=400&fit=crop',
            'content': "Bug-Bounty-Programme belohnen Forscher für das Finden von Schwachstellen.\n\n## Plattformen\n- **HackerOne**\n- **Bugcrowd**\n- **Intigriti** (Europa)\n\n## Häufige Schwachstellen\n- XSS, SQLi, CSRF, IDOR, SSRF\n\n## Einstieg\n1. OWASP Top 10 lernen\n2. HackerOne/Bugcrowd-Konto\n3. Programme mit gutem Ruf\n4. Jeden Fund dokumentieren\n\nBug Bounty = Fähigkeiten verbessern UND bezahlt werden!",
        },
    ],
}

def blog_list(request):
    from django.utils import translation
    lang = translation.get_language()
    articles = ARTICLES.get(lang, ARTICLES['en'])
    return render(request, 'blog/list.html', {'articles': articles})

def blog_detail(request, slug):
    from django.utils import translation
    from django.http import Http404
    lang = translation.get_language()
    articles = ARTICLES.get(lang, ARTICLES['en'])
    article = None
    for a in articles:
        if a['slug'] == slug:
            article = a
            break
    if not article:
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
