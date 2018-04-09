
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    # Includes
    path('tasks/', include('tasks.urls')),
]
