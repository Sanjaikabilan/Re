# Generated by Django 3.2.13 on 2022-05-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wisher', '0010_orga'),
    ]

    operations = [
        migrations.CreateModel(
            name='orig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secro', models.TextField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='orga',
            name='secro',
        ),
        migrations.AlterField(
            model_name='orga',
            name='ex',
            field=models.TextField(max_length=254),
        ),
    ]
