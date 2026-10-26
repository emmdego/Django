"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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

from Library.views import greetings, books, onSystem, template_books, book_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', greetings),
    path('book/', books),
    path('book/<str:name>/', books),
    path('book/<str:author>/', books),
    path('book/<str:name>/<str:author>/', books),
    path('to_system/', onSystem),
    path('t_books/', template_books, name="books"),
    path('t_books/details/', book_details, name="details")
]
