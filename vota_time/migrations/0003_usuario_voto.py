# Generated by Django 5.2 on 2025-04-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vota_time', '0002_remove_usuario_id_usario_usuario_id_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='voto',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
