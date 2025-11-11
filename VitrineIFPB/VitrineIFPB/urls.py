from django.contrib import admin

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('vitrine/', include('vitrine.urls'), name='vitrine'),
    path('administrador/', include('administrador.urls'), name='administrador'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)