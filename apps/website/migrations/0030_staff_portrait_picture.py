# Generated by Django 3.2 on 2023-12-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_auto_20231202_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='portrait_picture',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
