# Generated by Django 3.2.13 on 2022-05-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisher', '0003_alter_wishes_greetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishes',
            name='greetings',
            field=models.TextField(max_length=800),
        ),
    ]
