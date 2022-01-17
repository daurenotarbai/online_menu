from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu_app import views

urlpatterns = [

    path('<slug:slug>/', views.MenuView.as_view(), name='restaurant_menu'),
    path('auth/login', views.login_view, name='restaurant_login'),
    path('auth/logout', views.logout_view, name='logout_user'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
