"""
URL configuration for ExpressionsApp project.

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
from django.urls import include, path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from expressions.views import CustomLoginView, SignupView, main_menu

urlpatterns = [
    path("admin/", admin.site.urls),
    path('expressions/', include('expressions.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('', CustomLoginView.as_view(), name='login') , 
    # Définit la page de connexion comme racine
    path('menu/', main_menu, name='main_menu'),
    path('accounts/', include('django.contrib.auth.urls')),  # Assure que les autres vues auth sont disponibles
    
]
