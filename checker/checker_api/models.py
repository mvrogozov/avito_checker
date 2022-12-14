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

    check_date = models.ForeignKey(
        'CheckDate',
        verbose_name='Дата проверки',
        related_name='advert_counter',
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('search_phrase', 'region'),
                name='unique_pair'
            )
        ]

    def __str__(self):
        return f'{self.search_phrase[:10]} - {self.region}'


class CheckDate(models.Model):
    checked_date = models.DateTimeField(
        'Дата проверки'
    )

    counter = models.IntegerField(
        'Количество объявлений',
        help_text='Количество объявлений'
    )

    def __str__(self):
        return f'{self.checked_date}'
