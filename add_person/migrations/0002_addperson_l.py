# Generated by Django 2.0.1 on 2018-02-05 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addperson',
            name='l',
            field=models.BooleanField(default=True),
        ),
    ]
