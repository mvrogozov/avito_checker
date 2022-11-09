from django.contrib import admin
from typing import Callable, Sequence, Union
from .models import AdvertsCounter


class AdvertCounterAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str, Callable]] = (
        'id',
        'search_phrase',
        'region',
        'counter',
        'created'
    )


admin.site.register(AdvertsCounter, AdvertCounterAdmin)
