from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cases_app.views import CaseViewset

router = DefaultRouter()
router.register("cases", CaseViewset,basename="case")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
