import django_filters

from .models import ScoreEverything

class ScoreFilter(django_filters.FilterSet):
    class Meta:
        model = ScoreEverything
        fields = ['judge', 'candidate']
        