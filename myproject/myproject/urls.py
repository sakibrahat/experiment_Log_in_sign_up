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
# from django.urls import path
# from accounts import views

# urlpatterns = [
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.login_view, name='login'),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from accounts.views import signup

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', signup, name='signup'),  # Directly map the root URL to the signup view
#     path('accounts/', include('accounts.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.views import signup   # Import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Define URL pattern for the login page
    path('accounts/', include('accounts.urls')),
]



