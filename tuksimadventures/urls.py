from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('revoltadmin/', admin.site.urls),
    path('', include('tkadventure.urls')),
    path('', include('blog.urls'))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)