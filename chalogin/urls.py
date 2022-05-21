"""chaapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
# from chaapp.views import index, manage
from boardapp.views import index, post, login, logout, adminmain, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    # path('manage/', manage),
    path('', index),
    path('index/', index),
    path('index/<str:pageindex>/', index),
    path('post/', post),
    path('login/', login),
    path('logout/', logout),
    path('adminmain/', adminmain),
    path('adminmain/<str:pageindex>/', adminmain),
    path('delete/<int:boardid>/', delete),
    path('delete/<int:boardid>/<str:deletetype>/', delete),

    path('captcha/', include('captcha.urls')),
]