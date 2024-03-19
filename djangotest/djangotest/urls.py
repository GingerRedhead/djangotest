"""
URL configuration for djangotest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp.views import page_one, page_two, page_three
from django.contrib.flatpages import views

urlpatterns = [
    # ...
    path('admin/', admin.site.urls),
    path('page-one/', page_one, name='page-one'),
    path('page-two/', page_two, name='page-two'),
    path('page-three/', page_three, name='page-three'),
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    path('privacy/', views.flatpage, {'url': '/privacy/'}, name='privacy'),
    path('terms/', views.flatpage, {'url': '/terms/'}, name='terms'),
    path('my-page/', views.my_view, name='my-page'),
    # ...
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # ... Ваши другие URL-маршруты
]

