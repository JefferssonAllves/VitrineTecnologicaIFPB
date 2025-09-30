from django.urls import path, include

urlpatterns = [
    path('vitrine/', include('vitrine.urls'), name='vitrine'),
]
