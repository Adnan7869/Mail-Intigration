# Generated by Django 4.1.5 on 2023-01-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc_student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_civil',
            name='batch',
            field=models.CharField(choices=[('Medical', 'Medical'), ('Civil', 'Civil Engineering')], max_length=255),
        ),
    ]
