# Generated by Django 5.1.6 on 2025-02-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
