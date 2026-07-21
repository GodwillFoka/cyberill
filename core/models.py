from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'Demande générale'),
        ('audit', 'Audit & Conseil'),
        ('formation', 'Formation & Workshop'),
        ('pentest', 'Pentesting'),
        ('developpement', 'Développement d\'application'),
        ('partenariat', 'Partenariat'),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_subject_display()}] {self.name} — {self.email}"


class NewsletterSubscriber(models.Model):
    TOPIC_CHOICES = [
        ('all', 'Tous les sujets'),
        ('cybersecurity', 'Cybersécurité'),
        ('digital', 'Transformation digitale'),
        ('opportunities', 'Opportunités'),
    ]
    email = models.EmailField(unique=True)
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES, default='all')
    subscribed_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-subscribed_at']

    def __str__(self):
        return f"{self.email} ({self.get_topic_display()})"
