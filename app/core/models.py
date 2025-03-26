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


class TrainingDay(models.Model):

    DAY_CHOICES = [
        ("1", "Domingo"),
        ("2", "Segunda-feira"),
        ("3", "Terça-feira"),
        ("4", "Quarta-feira"),
        ("5", "Quinta-feira"),
        ("6", "Sexta-feira"),
        ("7", "Sábado"),
    ]

    DAY_ABBREVIATIONS = {
        "1": "Dom.",
        "2": "Seg.",
        "3": "Ter.",
        "4": "Qua.",
        "5": "Qui.",
        "6": "Sex.",
        "7": "Sáb.",
    }

    # Fields
    name = models.CharField("nome", max_length=100, choices=DAY_CHOICES, unique=True)
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)

    # Functions
    def __str__(self):
        return self.get_name_display()

    def get_abbreviation(self):
        return self.DAY_ABBREVIATIONS[self.name]

    class Meta:
        db_table = "training_day"
        verbose_name = "dia do treino"
        verbose_name_plural = "dias do treino"
        ordering = ["name"]


class User(AbstractUser):

    FREQUENCY_CHOICES = [
        ("1", "1x por semana"),
        ("2", "2x por semana"),
        ("3", "3x por semana"),
        ("4", "4x por semana"),
        ("5", "5x por semana"),
    ]

    TIME_CHOICES = [
        ("6", "06:00"),
        ("7", "07:00"),
        ("8", "08:00"),
        ("9", "09:00"),
        ("10", "10:00"),
        ("11", "11:00"),
        ("12", "12:00"),
        ("13", "13:00"),
        ("14", "14:00"),
        ("15", "15:00"),
        ("16", "16:00"),
        ("17", "17:00"),
        ("18", "18:00"),
        ("19", "19:00"),
        ("20", "20:00"),
        ("21", "21:00"),
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
    time = models.CharField(
        "horário",
        max_length=2,
        choices=TIME_CHOICES,
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
    training_days = models.ManyToManyField(
        TrainingDay,
        verbose_name="dias do treino",
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

    def list_of_training_days(self):
        return ", ".join(
            [
                training_day.get_abbreviation()
                for training_day in self.training_days.all()
            ]
        )

    list_of_training_days.short_description = "dias do treino"

    def list_of_groups(self):
        return ", ".join([group.name for group in self.groups.all()])

    list_of_groups.short_description = "grupos"

    class Meta:
        db_table = "core_user"
        verbose_name = "usuário"
        verbose_name_plural = "usuários"


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
