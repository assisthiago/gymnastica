# Generated by Django 5.1.7 on 2025-03-21 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_branch_options_alter_branch_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Administrador'), ('manager', 'Gerente'), ('trainer', 'Personal'), ('assistant', 'Assistente')], max_length=25, verbose_name='cargo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizado em')),
                ('branch', models.ManyToManyField(related_name='professionals', related_query_name='professional', to='core.branch', verbose_name='unidades')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='profissional')),
            ],
            options={
                'verbose_name': 'profissional',
                'verbose_name_plural': 'profissionais',
                'db_table': 'professional',
            },
        ),
    ]
