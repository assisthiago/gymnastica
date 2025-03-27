from django.contrib import admin

from app.core.models import User


class PersonalListFilter(admin.SimpleListFilter):

    title = "personal"
    parameter_name = "personal"

    def lookups(self, request, model_admin):
        return [
            (personal.id, personal.get_full_name())
            for personal in User.objects.filter(groups__in=[3])
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(personal__id=self.value())
