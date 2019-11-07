# Generated by Django 2.2.5 on 2019-10-20 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adsimages',
            name='ad_image',
            field=models.ImageField(blank=True, default='profile/None/no-img.jpg', null=True, upload_to='ads/'),
        ),
        migrations.AlterField(
            model_name='adsimages',
            name='ads',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='advert.Ads'),
        ),
    ]