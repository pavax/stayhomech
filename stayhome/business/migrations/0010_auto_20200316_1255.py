# Generated by Django 3.0.4 on 2020-03-16 12:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_business_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
