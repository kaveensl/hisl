# Generated by Django 4.1.2 on 2022-10-30 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CTF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='winners',
            name='Level',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
