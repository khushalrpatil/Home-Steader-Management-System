# Generated by Django 4.2.4 on 2024-02-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('approved', models.BooleanField(default=False)),
                ('image', models.ImageField(default=None, max_length=250, null=True, upload_to='images/')),
            ],
        ),
    ]