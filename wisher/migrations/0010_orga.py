# Generated by Django 3.2.13 on 2022-05-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisher', '0009_remove_prop_attach'),
    ]

    operations = [
        migrations.CreateModel(
            name='orga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex', models.EmailField(max_length=254)),
                ('secro', models.EmailField(max_length=254)),
            ],
        ),
    ]
