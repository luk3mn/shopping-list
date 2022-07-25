from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('item.urls')), # associa ao 'project' a url do app 'item'
    path('usuarios/', include('usuario.urls')),
]
