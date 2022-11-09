from .models import AdvertsCounter
from rest_framework import serializers
from rest_framework.decorators import action


class AdvertsCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertsCounter
        fields = (
            'id',
            'search_phrase',
            'region'
        )
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('search_phrase', 'region'),
                message=('Такой запрос уже существует.')
            )
        ]
