# Generated by Django 5.0.6 on 2024-06-13 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipicpay', '0007_rename_tipo_autorizacao_autorizacao_autorizacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioautorizacao',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apipicpay.usuario'),
        ),
    ]