from django.contrib import admin

import app.core.models as models


@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    fields = ("name", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("name",)
    search_help_text = "Busque pelo nome da unidade"


@admin.register(models.Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "list_branch",
        "list_group",
        "created_at",
        "updated_at",
    )
    fields = (
        "user",
        "branches",
        "list_group",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("list_group", "created_at", "updated_at")
    search_fields = ("user__first_name", "user__last_name")
    search_help_text = "Busque pelo nome do profissional"
    list_filter = ("branches",)


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "list_branch",
        "phone",
        "frequency",
        "updated_at",
    )
    fields = (
        "user",
        "branches",
        "cpf",
        "phone",
        "birth_date",
        "frequency",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at")
    search_fields = ("user__first_name", "user__last_name")
    search_help_text = "Busque pelo nome do cliente"
    list_filter = ("branches", "frequency")
