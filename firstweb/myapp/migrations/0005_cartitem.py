# Generated by Django 5.0.3 on 2024-03-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_shopitem_delete_ldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('pprice', models.CharField(max_length=10)),
                ('pimage', models.ImageField(upload_to='img')),
                ('ptotal', models.CharField(default=50, max_length=20)),
                ('pquantity', models.CharField(default=1, max_length=20)),
            ],
        ),
    ]
