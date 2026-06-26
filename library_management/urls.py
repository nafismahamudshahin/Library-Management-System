from django.contrib import admin
from django.urls import path , include
from .views import root_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include("api.urls"),name='api-root'),
    path('',root_view)
]
