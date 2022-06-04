# Generated by Django 4.0.4 on 2022-05-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_event_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('email', models.EmailField(max_length=254, verbose_name='')),
                ('subject', models.CharField(max_length=500, verbose_name='')),
                ('message', models.TextField(verbose_name='')),
            ],
        ),
    ]
