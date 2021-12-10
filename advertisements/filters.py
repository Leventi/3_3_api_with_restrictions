from django_filters import rest_framework as filters
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = filters.CharFilter(field_name='creator')
    created_at = filters.DateFromToRangeFilter()


    class Meta:
        model = Advertisement
        fields = []
