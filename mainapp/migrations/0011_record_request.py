# Generated by Django 3.2.9 on 2021-11-26 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mainapp.request'),
        ),
    ]
