from .models import AdvertsCounter, CheckDate
from rest_framework import serializers


class AdvertsCounterSerializer(serializers.ModelSerializer):
    check_date = serializers.PrimaryKeyRelatedField(
        read_only=True,
        )

    class Meta:
        model = AdvertsCounter
        fields = (
            'id',
            'search_phrase',
            'region',
            'check_date'
        )
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('search_phrase', 'region'),
                message=('Такой запрос уже существует.')
            )
        ]


class CheckDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckDate
        fields = ('checked_date', 'counter')
