# Generated by Django 3.2 on 2023-12-03 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_staff_portrait_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCertification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Project Certifications',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='certifications',
            field=models.ManyToManyField(to='website.ProjectCertification'),
        ),
    ]