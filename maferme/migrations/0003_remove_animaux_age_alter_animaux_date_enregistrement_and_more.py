# Generated by Django 5.0.6 on 2024-10-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maferme', '0002_animaux_date_enregistrement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animaux',
            name='age',
        ),
        migrations.AlterField(
            model_name='animaux',
            name='date_enregistrement',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animaux',
            name='date_naissance',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='animaux',
            name='sexe',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=10),
        ),
    ]
