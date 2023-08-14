from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
