# Generated by Django 4.0.4 on 2022-05-24 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_cadeira_projetos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='projetos',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto'),
        ),
    ]
