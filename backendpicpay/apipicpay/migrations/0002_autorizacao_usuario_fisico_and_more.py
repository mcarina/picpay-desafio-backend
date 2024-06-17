# Generated by Django 5.0.6 on 2024-06-13 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipicpay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorizacao',
            name='usuario_fisico',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='autorizacao',
            name='usuario_juridico',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='autorizacao',
            name='autorizacao',
            field=models.CharField(default='transicao', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='autorizacao',
            name='tipo_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autorizacoes', to='apipicpay.tipousuario'),
        ),
        migrations.CreateModel(
            name='SaldoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('autorizacao', models.BooleanField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apipicpay.usuario')),
            ],
        ),
    ]