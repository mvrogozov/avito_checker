from django.contrib import admin
from typing import Callable, Sequence, Union
from .models import AdvertsCounter, CheckDate


class AdvertCounterAdmin(admin.ModelAdmin):
    list_display: Sequence[Union[str, Callable]] = (
        'id',
        'search_phrase',
        'region',
    )


class CheckDateAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdvertsCounter, AdvertCounterAdmin)
admin.site.register(CheckDate, CheckDateAdmin)
