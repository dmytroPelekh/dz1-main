from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('categories/', include('categories.urls')),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
]

urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)