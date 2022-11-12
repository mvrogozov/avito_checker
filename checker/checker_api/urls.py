from django.urls import include, path
from .views import AdvertCounterStatViewSet, AdvertCounterAddView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(
    'counters/stat',
    AdvertCounterStatViewSet,
    basename='api_counters'
)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'counters/add/',
        AdvertCounterAddView.as_view(),
        name='api_advert_add'
    )
]
