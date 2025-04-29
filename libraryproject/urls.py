import apps.bookmodule.views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")),
    path('', apps.bookmodule.views.index),
    path('index2/<int:val1>/', apps.bookmodule.views.index2),
    path('users/', include("apps.usermodule.urls")),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
