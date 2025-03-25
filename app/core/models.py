from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class Branch(models.Model):

    # Fields
    name = models.CharField("nome", max_length=100)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Functions
    def __str__(self):
        return self.name

    class Meta:
        db_table = "branch"
        verbose_name = "unidade"
        verbose_name_plural = "unidades"
        ordering = ["name"]


class User(AbstractUser):

    FREQUENCY_CHOICES = [
        ("1", "1x por semana"),
        ("2", "2x por semana"),
        ("3", "3x por semana"),
        ("4", "4x por semana"),
        ("5", "5x por semana"),
        ("6", "6x por semana"),
        ("7", "7x por semana"),
    ]

    # Fields
    cpf = models.CharField(
        "cpf",
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
        default=None,
    )
    phone = models.CharField(
        "telefone",
        max_length=11,
        unique=True,
        validators=[MinLengthValidator(11)],
        blank=True,
        null=True,
        default=None,
    )
    birth_date = models.DateField(
        "data de nascimento",
        blank=True,
        null=True,
        default=None,
    )
    frequency = models.CharField(
        "frequência",
        max_length=1,
        choices=FREQUENCY_CHOICES,
        blank=True,
        null=True,
        default=None,
    )

    # Relationships
    branches = models.ManyToManyField(
        Branch,
        verbose_name="unidades",
        related_name="users",
    )

    # Settings
    USERNAME_FIELD = "username"

    # Functions
    def __str__(self):
        return self.get_full_name()

    def full_name(self):
        return self.__str__()

    full_name.short_description = "nome"

    def list_of_branches(self):
        return ", ".join([branch.name for branch in self.branches.all()])

    list_of_branches.short_description = "unidades"

    def list_of_groups(self):
        return ", ".join([group.name for group in self.groups.all()])

    list_of_groups.short_description = "grupos"

    class Meta:
        db_table = "core_user"
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
        ordering = ["first_name", "last_name"]


class Training(models.Model):

    # Fields
    date = models.DateField("data")
    time = models.TimeField("horário")
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Relationships
    branch = models.ForeignKey(
        Branch,
        verbose_name="unidade",
        on_delete=models.CASCADE,
        related_name="trainings",
    )
    personal = models.ForeignKey(
        User,
        verbose_name="personal",
        on_delete=models.CASCADE,
        related_name="personal_trainings",
    )
    clients = models.ManyToManyField(
        User,
        verbose_name="clientes",
        related_name="client_trainings",
    )

    class Meta:
        db_table = "training"
        verbose_name = "treino"
        verbose_name_plural = "treinos"
        ordering = ["date", "time"]
        constraints = [
            models.UniqueConstraint(
                fields=["date", "time", "branch", "personal"],
                name="unique_training",
            )
        ]
