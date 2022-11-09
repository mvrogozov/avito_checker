from django.urls import include, path
from .views import AdvertCounterViewSet, AdvertCounterAddView
from rest_framework import routers


router = routers.DefaultRouter()
#router.register('counters', AdvertCounterViewSet, basename='api_counters')

urlpatterns = [
    path('', include(router.urls)),
    path('counters/add/', AdvertCounterAddView.as_view(), name='api_advert_add')
]
