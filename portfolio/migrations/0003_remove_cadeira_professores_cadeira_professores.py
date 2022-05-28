# Generated by Django 4.0.4 on 2022-05-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_cadeira_link_alter_cadeira_projetos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadeira',
            name='professores',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professores',
            field=models.ManyToManyField(to='portfolio.pessoa'),
        ),
    ]
