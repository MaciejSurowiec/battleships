# Generated by Django 4.2.3 on 2023-10-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battleships', '0004_alter_board_ships_element_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='current_player',
            field=models.IntegerField(default=1),
        ),
    ]
