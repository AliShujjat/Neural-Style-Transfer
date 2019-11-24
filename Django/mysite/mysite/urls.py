"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from myapp import views as v
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', v.index, name = "index"),
    #path('actionUrl', v.content_image_view, name = 'image_upload'),
    path('image_upload', v.content_image_view, name = 'image_upload'),
    #path('display_content_images', v.display_content_images, name = 'content_images'),
    path('success', v.success, name = 'success'),
    path('final_image', v.final_image, name = 'final_image')
] 

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT) 
