# Generated by Django 5.1.3 on 2024-11-28 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('nivel', models.CharField(choices=[('F', 'Fácil'), ('M', 'Médio'), ('D', 'Difícil')], max_length=1)),
                ('alternativa_a', models.CharField(max_length=255)),
                ('alternativa_b', models.CharField(max_length=255)),
                ('alternativa_c', models.CharField(max_length=255)),
                ('alternativa_d', models.CharField(max_length=255)),
                ('resposta_correta', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(auto_now_add=True)),
                ('pontuacao_final', models.IntegerField(default=0)),
                ('nivel_atual', models.CharField(choices=[('F', 'Fácil'), ('M', 'Médio'), ('D', 'Difícil')], max_length=1)),
                ('jogador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.jogador')),
            ],
        ),
    ]