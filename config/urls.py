from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

handler404 = 'core.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', RedirectView.as_view(url=staticfiles_storage.url('robots.txt'))),
    path('sitemap.xml', RedirectView.as_view(url=staticfiles_storage.url('sitemap.xml'))),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
