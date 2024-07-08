"""
URL configuration for myproject project.

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
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('travelguide/',views.travelguide),
    path('invest/',views.invest),
    path('contact/',views.contact),
    path('about/',views.about),
    path('place/',views.place),
    path('culture/',views.culture),
    path('food/',views.food),
    path('art/',views.art),
    path('wildlife/',views.wildlife),
    path('top10/',views.top10),
    path('guidelines/',views.guidelines),
    path('artandcraft/',views.artandcraft),
    path('wildlifeandnature/', views.wildlifeandnature),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


