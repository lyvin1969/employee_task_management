from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # Redirect root URL '/' directly to the dashboard
    path("", lambda request: redirect("dashboard:dashboard")),

    path("admin/", admin.site.urls),

    path("accounts/", include("accounts.urls")),

    path("employees/", include("employees.urls")),
    
    path("departments/", include("departments.urls")),
    
    path("tasks/", include("tasks.urls")),
    
    path("notifications/", include("notifications.urls")),
    
    path("reports/", include("reports.urls")),
    
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )