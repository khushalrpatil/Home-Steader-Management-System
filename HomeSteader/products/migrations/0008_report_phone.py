# Generated by Django 4.2.4 on 2024-06-28 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_report_city_report_state_report_street_report_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='phone',
            field=models.IntegerField(blank=True, default=1, max_length=12, null=True),
        ),
    ]