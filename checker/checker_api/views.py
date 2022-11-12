from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import AdvertsCounter, CheckDate
from .serializers import AdvertsCounterSerializer
from .utils import count_adverts
from django.utils import timezone


class AdvertCounterViewSet(ModelViewSet):
    queryset = AdvertsCounter.objects.all()
    serializer_class = AdvertsCounterSerializer

    @action(
        detail=False,
        methods=['post']
    )
    def add(self, request):
        pass


class AdvertCounterAddView(APIView):
    def post(self, request):
        search_phrase = request.data.get('search_phrase').lower()
        region = request.data.get('region').lower()
        request.data['region'] = region
        request.data['search_phrase'] = search_phrase
        url = 'https://www.avito.ru'
        counter = str(count_adverts(url, region, search_phrase))
        print('type = ', type(counter))
        print( ' val= ', counter.replace('\xa0', ''))
        #request.data['counter'] = int(counter.replace('\xa0', ''))
        serializer = AdvertsCounterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        check_date = CheckDate.objects.create(
            checked_date=timezone.now(),
            counter=int(counter)
        )
        adv_obj = AdvertsCounter.objects.get(id=serializer.data['id'])
        adv_obj.check_date = check_date
        adv_obj.save()
        return Response(
            {"id": serializer.data['id']}, status=status.HTTP_201_CREATED
        )


class AdvertCounterStatViewSet(ModelViewSet):
    queryset = AdvertsCounter.objects.select_related('check_date')
    serializer_class = AdvertsCounterSerializer
