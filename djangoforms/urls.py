from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('myapp.urls')),  # Ensure this points to your blog app
]
