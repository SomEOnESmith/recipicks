# Generated by Django 2.2.6 on 2019-11-05 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191103_1137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='total_time',
            field=models.DurationField(default='00:00:00'),
        ),
    ]
