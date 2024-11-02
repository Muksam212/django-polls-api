import django_filters
from users.models import User
from polls.models import Choice

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username", lookup_expr="iexact")
    email = django_filters.CharFilter(field_name = "email", lookup_expr="iexact")
    class Meta:
        model = User
        fields = ("username", "email")


class ChoiceFilter(django_filters.FilterSet):
    poll = django_filters.CharFilter(field_name = "poll__question", lookup_expr="iexact")

    class Meta:
        model = Choice
        fields = ("poll__question",)