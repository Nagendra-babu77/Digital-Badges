from django.urls import path
from App.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('UploadBadge/',upload_badge,name="UploadBadge"),
    path('ListofBadges/',badges_list,name="badges_list"), 
    path('ListofBadges/getbadge/<int:pk>/',get_badge,name="get_badge"), 
    path('ListofBadges/delete/<int:pk>/',delete_badge,name="delete_badge"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)