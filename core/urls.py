from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('ressources/', views.ressources, name='ressources'),
    path('stats/', views.stats_cyber, name='stats'),
    path('cv/', views.cv_page, name='cv'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('brand/', views.brand_kit, name='brand'),
    path('brand/signature/', views.brand_email_signature, name='brand_email_signature'),
    path('brand/signature-outlook/', views.brand_email_signature_outlook, name='brand_email_signature_outlook'),
    path('book/', views.book_mode, name='book_mode'),
    path('premium/', views.home_premium, name='home_premium'),
    path('clean/', views.home_clean, name='home_clean'),
    path('cv/download/', views.cv_download, name='cv_download'),
]
