from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
   # path('password/', include('django.contrib.auth.urls')),
]
