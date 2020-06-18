"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
    path('',include('home.urls')),
   # path('SIGNUP1/',include('SIGNUP1.urls')),
    path('SIGNUP2/',include('SIGNUP2.urls')),
    path('LOGIN/',include('LOGIN.urls')),
    path('ABOUT/',include('ABOUT.urls')),
    path('CONTACTUS/',include('CONTACTUS.urls')),
    #path('GALLERY/',include('GALLERY.urls')),
    path('EXAMAPP/',include('EXAMAPP.urls')),
    path('STUDENT_DATA/',include('STUDENT_DATA.urls')),
    path('IMAGE_G/',include('IMAGE_G.urls')),
    path('GALLERy1/', include('GALLERy1.urls')),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)