INSTALLED_APPS = [
    ...
    'myapp',
]

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, Django!</h1><p>Welcome to my first Django web page.</p>")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
