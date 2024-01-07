# Generated by Django 3.2 on 2023-12-01 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0026_alter_projectlead_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlead',
            name='name',
            field=models.CharField(blank=True, default='Tree', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='projectlead',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.staff'),
        ),
    ]
