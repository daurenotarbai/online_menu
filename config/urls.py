from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from menu_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include("menu_app.urls")),
    path('', views.MainView.as_view(), name='main'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)