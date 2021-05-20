from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('auth/', include('authapp.urls', namespace='authapp')),
    path('', include('mainapp.urls', namespace='mainapp')),

    path('admin/', admin.site.urls),

    path('summernote/', include('django_summernote.urls')),

]
