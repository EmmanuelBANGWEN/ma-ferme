# Generated by Django 5.0.6 on 2024-10-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maferme', '0003_remove_animaux_age_alter_animaux_date_enregistrement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaux',
            name='date_enregistrement',
            field=models.DateField(auto_now_add=True),
        ),
    ]
