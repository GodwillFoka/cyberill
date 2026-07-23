from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        # Phase 1 : notification sans BDD
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', 'general')
        messages.success(
            request,
            f'Merci {name} ! Votre message a été reçu. '
            f'Je vous répondrai à {email} dans les plus brefs délais.'
        )
        return render(request, 'core/contact.html')
    return render(request, 'core/contact.html')

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        messages.success(
            request,
            f'Merci ! {email} est inscrit à la newsletter CYBERILL.'
        )
    return redirect(request.META.get('HTTP_REFERER', '/'))
