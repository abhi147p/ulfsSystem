# Generated by Django 4.2.7 on 2023-12-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_lostitem_image_alter_founditem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='lost_item_images/'),
        ),
    ]
