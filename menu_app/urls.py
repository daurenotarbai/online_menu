from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menu_app import views

urlpatterns = [

    path('<slug:slug>/', views.MenuView.as_view(), name='restaurant_menu'),
    path('create/product', views.ProductCreateView.as_view(), name='create_product'),
    path('update/product/<slug:pk>/', views.ProductUpdateView.as_view(), name='update_product'),
    path('delete/product/<slug:pk>/', views.ProductDeleteView.as_view(), name='delete_product'),

    path('create/category', views.CategoryCreateView.as_view(), name='create_category'),
    path('update/category/<slug:pk>/', views.CategoryUpdateView.as_view(), name='update_category'),
    path('delete/category/<slug:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),

    path('auth/login', views.login_view, name='restaurant_login'),
    path('auth/logout', views.logout_view, name='logout_user'),
    path('update/product-status/<slug:pk>/', views.update_product_status, name='update_product_status'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
