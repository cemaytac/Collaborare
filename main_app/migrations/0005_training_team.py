# Generated by Django 3.1.1 on 2020-10-13 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201013_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.team'),
            preserve_default=False,
        ),
    ]
