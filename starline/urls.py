"""starline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main import viewsAPI

router = routers.DefaultRouter()
router.register(r'comments', viewsAPI.CommentViewSet)
router.register(r'popular_product', viewsAPI.PopularProductViewSet)
router.register(r'our_work', viewsAPI.OurWorkViewSet)
router.register(r'category_search', viewsAPI.CategotyFiltViewSet)
router.register(r'novelties', viewsAPI.NoveltiesProductViewSet)
router.register(r'product', viewsAPI.ProductViewSet)
router.register(r'all_category', viewsAPI.CategoryViewSet)
router.register(r'characteristic', viewsAPI.CharacteristicSerializerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('starline/', include(router.urls)),
]

handler404 = 'main.views.error'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

