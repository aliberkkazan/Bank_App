from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('customer_account.api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/dj-rest-auth/',include('dj_rest_auth.urls')),
]
