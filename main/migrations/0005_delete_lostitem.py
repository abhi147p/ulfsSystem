# Generated by Django 4.2.7 on 2023-12-04 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_founditem_image_alter_lostitem_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LostItem',
        ),
    ]