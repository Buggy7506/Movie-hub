from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import MovieViewSet  


router = DefaultRouter()
router.register(r'movies', MovieViewSet)


urlpatterns = [
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('dashboard-data/', views.dashboard_data, name='dashboard_data'),
    path('api/', include(router.urls)),
]











