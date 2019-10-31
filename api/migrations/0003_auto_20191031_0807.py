# Generated by Django 2.2.6 on 2019-10-31 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_step_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='step',
            name='required_time',
            field=models.PositiveIntegerField(),
        ),
    ]
