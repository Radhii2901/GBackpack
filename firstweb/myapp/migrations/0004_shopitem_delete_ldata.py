# Generated by Django 5.0.3 on 2024-03-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_fname_sdata_fnm_rename_lname_sdata_lnm'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=20)),
                ('pprice', models.CharField(max_length=10)),
                ('pimage', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.DeleteModel(
            name='ldata',
        ),
    ]