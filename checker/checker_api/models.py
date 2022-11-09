from django.db import models


class AdvertsCounter(models.Model):
    search_phrase = models.CharField(
        'Поисковая фраза',
        max_length=200,
        null=False,
        blank=False
    )

    region = models.CharField(
        'Регион',
        max_length=200,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
        help_text='Дата создания запроса'
    )

    counter = models.IntegerField(
        'Количество объявлений',
        help_text='Количество объявлений'
    )

    def __str__(self):
        return f'{self.search_phrase[:10]} - {self.region}'
