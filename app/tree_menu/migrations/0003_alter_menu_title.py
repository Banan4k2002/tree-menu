# Generated by Django 4.2.14 on 2024-07-26 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "tree_menu",
            "0002_alter_menu_options_alter_menuitem_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="title",
            field=models.CharField(
                max_length=128, unique=True, verbose_name="Название"
            ),
        ),
    ]
