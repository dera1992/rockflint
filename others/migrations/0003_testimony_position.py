# Generated by Django 2.2.5 on 2019-11-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_testimony'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimony',
            name='position',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]