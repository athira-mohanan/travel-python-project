# Generated by Django 4.2.3 on 2023-07-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_travel_app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='pics')),
                ('profile', models.TextField()),
            ],
        ),
    ]
