
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/app/', include('app.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
    path('auth_a/', include('djoser.urls.jwt')),
]

