# Generated by Django 3.2.9 on 2022-02-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_alter_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='kino_aktyorlari', to='film.Actor'),
        ),
    ]
