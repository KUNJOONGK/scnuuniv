from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from homepage import views
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hompage),
    path('account/', include('account.urls')),
]
