# Generated by Django 5.0.3 on 2024-03-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('femail', models.CharField(max_length=20)),
                ('fcmt', models.CharField(max_length=20)),
            ],
        ),
    ]
