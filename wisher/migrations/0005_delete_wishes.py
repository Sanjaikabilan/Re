# Generated by Django 3.2.13 on 2022-05-13 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisher', '0004_alter_wishes_greetings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishes',
        ),
    ]