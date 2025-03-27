from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from app.core.filters import PersonalListFilter
from app.core.forms import TrainingForm
from app.core.models import Branch, Training, TrainingDay, User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):

    # Queryset
    def get_queryset(self, request):
        qs = super().get_queryset(request).prefetch_related("branches")
        return qs.filter(~Q(pk=1))

    # Add/Change view
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "cpf",
                    "phone",
                    "birth_date",
                )
            },
        ),
        (
            _("Academia"),
            {"fields": ("branches", "training_days", "time")},
        ),
        (
            _("Permissões"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                ),
            },
        ),
        (_("Datas importantes"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ["last_login", "date_joined"]
    filter_horizontal = ["groups", "branches", "training_days"]

    # Change list view
    list_display = [
        "change_link",
        "full_name",
        "list_of_groups",
        "list_of_branches",
        "list_of_training_days",
        "time",
        "is_active",
    ]
    list_display_links = ["change_link"]
    list_filter = ["is_active", "groups", "branches", "time"]
    search_fields = ["first_name", "last_name", "email", "cpf", "phone"]
    search_help_text = _("Pesquisar por nome, sobrenome, email ou CPF.")
    ordering = ["groups", "first_name", "last_name"]

    @admin.display(description="#")
    def change_link(self, _):
        return "Ver detalhes"


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = [
        "change_link",
        "name",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["change_link"]

    @admin.display(description="#")
    def change_link(self, _):
        return "Ver detalhes"


@admin.register(TrainingDay)
class TrainingDayAdmin(admin.ModelAdmin):

    # Change list view
    list_display = [
        "name",
    ]


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):

    # Add/Change view
    form = TrainingForm
    fieldsets = (
        (None, {"fields": ("date", "time", "branch")}),
        (
            _("Atendimento"),
            {
                "fields": (
                    "personal",
                    "clients",
                )
            },
        ),
        (
            _("Datas importantes"),
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    filter_horizontal = ["clients"]
    radio_fields = {"personal": admin.VERTICAL}
    readonly_fields = ["created_at", "updated_at"]

    # Change list view
    date_hierarchy = "date"
    list_display = [
        "change_link",
        "date",
        "time_formatted",
        "day_of_week",
        "personal",
        "list_of_clients",
        "branch",
    ]
    list_display_links = ["change_link"]
    list_filter = [PersonalListFilter, "branch", "date"]
    search_fields = [
        "personal__first_name",
        "personal__last_name",
        "clients__first_name",
        "clients__last_name",
    ]
    search_help_text = _("Pesquisar por nome personal ou do cliente.")
    ordering = ["-date", "time"]

    @admin.display(description="#")
    def change_link(self, _):
        return "Ver detalhes"
