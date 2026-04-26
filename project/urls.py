from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>JetFlow Demo</h1><p>CI/CD is running!</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
