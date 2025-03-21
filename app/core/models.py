from django.contrib.auth.models import Group, User
from django.db import models


class Branch(models.Model):
    name = models.CharField("nome", max_length=100)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "branch"
        verbose_name = "unidade"
        verbose_name_plural = "unidades"
        ordering = ["name"]


class Professional(models.Model):
    ROLE_CHOICES = {
        "admin": "Administrador",
        "manager": "Gerente",
        "trainer": "Personal",
        "assistant": "Assistente",
    }

    user = models.OneToOneField(
        User, verbose_name="profissional", on_delete=models.CASCADE
    )
    branches = models.ManyToManyField(
        Branch,
        verbose_name="unidades",
        related_name="professionals",
        related_query_name="professional",
    )
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # Fields
    def full_name(self):
        return self.__str__()

    full_name.short_description = "nome"

    def list_branch(self):
        return ", ".join([branch.name for branch in self.branches.all()])

    list_branch.short_description = "unidades"

    def list_group(self):
        return ", ".join([group.name for group in self.user.groups.all()])

    list_group.short_description = "cargos"

    class Meta:
        db_table = "professional"
        verbose_name = "profissional"
        verbose_name_plural = "profissionais"
        ordering = ["user__first_name", "user__last_name"]
