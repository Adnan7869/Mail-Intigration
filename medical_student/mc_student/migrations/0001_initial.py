# Generated by Django 4.1.5 on 2023-01-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_Civil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('college_name', models.CharField(max_length=255)),
                ('batch', models.CharField(max_length=255)),
                ('cotact', models.BigIntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
