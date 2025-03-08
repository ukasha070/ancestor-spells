from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from base.views import login_view

urlpatterns = [
    path("admin/login/", login_view, name='admin-login'),
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('services/', include('service.urls')),
    
    path(r'mdeditor/', include('mdeditor.urls'))
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
