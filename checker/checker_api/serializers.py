from .models import AdvertsCounter
from rest_framework import serializers


class AdvertsCounterSerializer(serializers.ModelSerializer):
    counter = serializers.IntegerField()

    class Meta:
        model = AdvertsCounter
        fields = (
            'id',
            'search_phrase',
            'region',
            'counter'
        )
