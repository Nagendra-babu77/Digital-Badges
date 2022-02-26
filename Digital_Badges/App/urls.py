from django.urls import path
from App.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('UploadBadge/',upload_badge,name="UploadBadge") 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)