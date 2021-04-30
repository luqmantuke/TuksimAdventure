from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = [
    path('revoltadmin/', admin.site.urls),
    path('', include('tkadventure.urls')),
    path('', include('blog.urls')),
    path("robots.txt", TemplateView.as_view(template_name="Robots.txt", content_type="text/plain"),),
    path("sitemap.xml", TemplateView.as_view(template_name="sitemap.xml"),),
]



handler404 = 'tkadventure.views.handler404'
handler500 = 'tkadventure.views.handler500'

