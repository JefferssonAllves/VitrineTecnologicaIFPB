from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('vitrine/', include('vitrine.urls'), name='vitrine'),
    path('institucional/', include('institucional.urls'), name='institucional'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)