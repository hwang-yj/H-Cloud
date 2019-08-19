from django.urls import path
from . import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'versions',views.VersionViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
