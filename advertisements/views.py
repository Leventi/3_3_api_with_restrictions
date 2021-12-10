from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import DeleteIfOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()

    def list(self, request):
        if request.auth is None:
            queryset = Advertisement.objects.exclude(status='DRAFT')
        else:
            all_adv_without_draft = Advertisement.objects.exclude(status='DRAFT')
            draft_adv_for_auth_user = Advertisement.objects.filter(creator__username=request.user.username, status='DRAFT')
            queryset = all_adv_without_draft | draft_adv_for_auth_user

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), DeleteIfOwner()]
        return []
