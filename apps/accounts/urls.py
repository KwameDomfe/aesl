
"""aeslWebAppdir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from . views import (
    userlogin_view,
    userlogout_view,
    userRegister_view, 
)
from . adminViews import (
    admin_Home,
    admin_Login,
    admin_logout,
    
)
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path("user-login", 
        userlogin_view, 
        name="user-login"),
    path("user-logout", 
        userlogout_view, 
        name="user-logout"),
    path("register", 
        userRegister_view, 
        name="user-register"),

    path(
        'admin-login/', 
        admin_Login, 
        name='admin-login'
    ), 
    path('admin-home/', 
        admin_Home, 
        name='admin-home'
    ),
   
    # path('admin-login-process/', 
    #     admin_Login_Process, 
    #     name='admin-login-process'
    # ),
    # path('staff-login/', 
    #     staff_Login, 
    #     name='staff-login'), 

   
]