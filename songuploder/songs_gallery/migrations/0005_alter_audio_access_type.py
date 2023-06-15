# Generated by Django 4.2.2 on 2023-06-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs_gallery', '0004_protectedfileaccess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='access_type',
            field=models.CharField(choices=[('Protected', 'Protected'), ('Private', 'Private'), ('Public', 'Public')], max_length=20),
        ),
    ]
