# Generated by Django 3.2 on 2023-11-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20231128_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Client Name')),
                ('postal_address', models.CharField(max_length=128, verbose_name='Postal Address')),
                ('website', models.CharField(max_length=50, verbose_name='Website')),
            ],
        ),
    ]