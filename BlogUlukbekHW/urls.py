"""
URL configuration for BlogUlukbekHW project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts_views.main_view),
    path('products/', posts_views.products_view),
    path('products/<int:id>/', posts_views.detail_view),
    path('categories/', posts_views.categories_view),
    path('products/create_categories/', posts_views.create_categories_view),
    path('products/create_products/', posts_views.create_products_view),

    path('users/register/', users_views.register_view),
    path('users/auth/', users_views.auth_view),
    path('users/logout/', users_views.logout_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)