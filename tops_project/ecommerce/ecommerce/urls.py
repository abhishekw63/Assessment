"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecommerceapp.urls')),
    path('auth/',include('authcart.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# In a Django project, MEDIA_URL and MEDIA_ROOT are settings used for handling media files

# This setting defines the base URL for serving media files.
# Example: If MEDIA_URL is set to '/media/', then media files will be served under URLs like http://example.com/media/filename.jpg.

# this setting defines the absolute filesystem path to the directory that will hold the media files.
# Example: If MEDIA_ROOT is set to '/path/to/media/', then the server will look for media files in this directory.