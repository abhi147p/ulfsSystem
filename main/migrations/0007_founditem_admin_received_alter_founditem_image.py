# Generated by Django 4.2.7 on 2023-12-04 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_founditemtimeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='admin_received',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='founditem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='found_item_images/'),
        ),
    ]
