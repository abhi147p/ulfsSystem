# Generated by Django 4.2.7 on 2023-12-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_lostitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/found_item_images/'),
        ),
        migrations.AlterField(
            model_name='lostitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/lost_item_images/'),
        ),
    ]