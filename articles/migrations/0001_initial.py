# Generated by Django 3.2.5 on 2024-11-24 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ti', models.TextField()),
                ('co', models.TextField()),
            ],
        ),
    ]
