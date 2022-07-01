from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), # associa ao 'project' a urls do app 'main'
    path('item', include('item.urls')), # associa ao 'project' a url do app 'item'
]
