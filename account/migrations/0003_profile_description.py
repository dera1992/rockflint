# Generated by Django 2.2.5 on 2019-10-26 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]