from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
    path('ressources/', views.ressources, name='ressources'),
    path('stats/', views.stats_cyber, name='stats'),
    path('cv/', views.cv_page, name='cv'),
]
