# Generated by Django 5.2.1 on 2025-06-06 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_grupopesquisa_area_grupopesquisa_imagem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('imagem', models.ImageField(upload_to='destaques/')),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='grupopesquisa',
            name='area',
        ),
        migrations.RemoveField(
            model_name='grupopesquisa',
            name='imagem',
        ),
        migrations.RemoveField(
            model_name='grupopesquisa',
            name='site',
        ),
    ]
