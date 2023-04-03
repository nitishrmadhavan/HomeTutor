
from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
#for images
from django.conf.urls.static import static  
#helps us to create url for static files
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faq/',views.faq,name="faq"),
    path('projects/',include('projects.urls')),
    path('',include('users.urls')),
    path('api/',include('api.urls')),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reser_password.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),name="password_reset_complete"),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#for images