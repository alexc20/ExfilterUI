# Generated by Django 4.0.2 on 2022-02-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='egressevent',
            old_name='daddr',
            new_name='Daddr',
        ),
        migrations.RenameField(
            model_name='egressevent',
            old_name='data',
            new_name='Data',
        ),
        migrations.RenameField(
            model_name='egressevent',
            old_name='msg',
            new_name='Msg',
        ),
        migrations.RenameField(
            model_name='egressevent',
            old_name='pid',
            new_name='Pid',
        ),
        migrations.RenameField(
            model_name='egressevent',
            old_name='saddr',
            new_name='Saddr',
        ),
        migrations.RenameField(
            model_name='egressevent',
            old_name='timestamp',
            new_name='Timestamp_ns',
        ),
    ]