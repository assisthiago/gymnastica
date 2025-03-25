from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _

from app.core.models import Branch, Training, User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):

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
            {
                "fields": (
                    "branches",
                    "frequency",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    readonly_fields = ["last_login", "date_joined"]
    filter_horizontal = ["groups", "user_permissions", "branches"]
    radio_fields = {"frequency": admin.VERTICAL}

    # Change list view
    list_display = [
        "change_link",
        "full_name",
        "list_of_groups",
        "list_of_branches",
        "frequency",
        "is_active",
    ]
    list_display_links = ["change_link"]

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


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):

    # Change list view
    list_display = [
        "change_link",
        "date",
        "time",
        "branch",
    ]
    list_display_links = ["change_link"]

    list_filter = ["branch"]

    @admin.display(description="#")
    def change_link(self, _):
        return "Ver detalhes"
