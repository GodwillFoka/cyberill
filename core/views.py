from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject', 'general'),
            message=request.POST.get('message'),
        )
        messages.success(request, 'Message envoyé avec succès ! Je vous répondrai dans les plus brefs délais.')
        return redirect('contact')
    return render(request, 'core/contact.html')

def newsletter_signup(request):
    if request.method == 'POST':
        from .models import NewsletterSubscriber
        NewsletterSubscriber.objects.create(
            email=request.POST.get('email'),
            topic=request.POST.get('topic', 'all'),
        )
        messages.success(request, 'Inscription réussie ! Merci de votre intérêt.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))
