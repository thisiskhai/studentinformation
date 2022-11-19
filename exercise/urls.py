
from django.contrib import admin
from django.urls import path
from Formings.views import (
    create, 
    show, 
    detail, 
    deleteInfo,
    update)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", create),
    path("show/", show),
    path("show/<pk>/", detail),
    path("show/<pk>/delete/", deleteInfo),    
    path("show/<pk>/update/", update),    
]
