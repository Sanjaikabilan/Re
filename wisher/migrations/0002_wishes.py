# Generated by Django 3.2.13 on 2022-05-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greetings', models.CharField(max_length=1000)),
            ],
        ),
    ]
