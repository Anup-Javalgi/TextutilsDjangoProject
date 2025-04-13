"""
URL configuration for textutils project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    # path("about/", views.about, name="about"),  # (endpoints)url ke badd kya append karna hai, it is a function when u go to about, it is name of path
    # django will first come into url section then go to the views section according to the functions and execute them.
    # path("textfile/", views.text, name="textfile"),
    # path("removepunc", views.removepunc, name="rempun"),
    # path("capitalizefirst", views.capfirst, name="capfirst"),
    # path("newlineremove", views.newlineremove, name="newlineremove"),
    # path("spaceremove", views.spaceremove, name="spaceremove"),
    # path("charcount", views.charcount, name="charcount")
    path('analyze', views.analyze, name="analyze")
]
