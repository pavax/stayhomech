# Generated by Django 3.0.4 on 2020-03-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20200316_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handled', models.BooleanField(default=False)),
                ('data', models.TextField()),
            ],
        ),
    ]
