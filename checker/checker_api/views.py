from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import AdvertsCounter
from .serializers import AdvertsCounterSerializer


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
        request.data['region'] = request.data.get('region').lower()
        request.data['search_phrase'] = (
            request.data.get('search_phrase').lower()
        )
        serializer = AdvertsCounterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"id": serializer.data['id']}, status=status.HTTP_201_CREATED
        )
