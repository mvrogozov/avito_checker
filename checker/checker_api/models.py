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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('search_phrase', 'region'),
                name='unique_pair'
            )
        ]

    def __str__(self):
        return f'{self.search_phrase[:10]} - {self.region}'
