# Generated by Django 2.2.6 on 2019-11-27 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20191128_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
    ]
