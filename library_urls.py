from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import AdminSignupView, AdminLoginView
from books.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('api/auth/login/', AdminLoginView.as_view(), name='admin-login'),
    path('api/', include(router.urls)),
]
