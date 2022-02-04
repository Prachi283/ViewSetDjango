from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

# Createing Router Object
router= DefaultRouter()

# Register EmployeeViewSet with Router
router.register('employeeapi',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
