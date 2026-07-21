from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['subject', 'read', 'created_at']
    search_fields = ['name', 'email', 'message']
    date_hierarchy = 'created_at'

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'topic', 'subscribed_at', 'active']
    list_filter = ['topic', 'active', 'subscribed_at']
    search_fields = ['email']
