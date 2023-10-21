import django_filters
from .models import RegisteredGroup, Group, Profile


class RegisteredGroupFilter(django_filters.FilterSet):
    group_tg_id = django_filters.CharFilter(field_name='group_tg_id')

    class Meta:
        model = RegisteredGroup
        fields = ['group_tg_id', 'is_active']


class GroupFilter(django_filters.FilterSet):
    group_tg = django_filters.CharFilter(field_name='group_tg')

    class Meta:
        model = Group
        fields = ['group_tg']


class ProfileFilter(django_filters.FilterSet):
    tg_id = django_filters.CharFilter(field_name='tg_id')

    class Meta:
        model = Profile
        fields = ['tg_id']
