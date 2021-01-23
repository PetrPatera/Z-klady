# Generated by Django 3.1.4 on 2021-01-04 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zanr',
            name='film',
        ),
        migrations.AddField(
            model_name='film',
            name='zanr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moviebook.zanr'),
        ),
    ]