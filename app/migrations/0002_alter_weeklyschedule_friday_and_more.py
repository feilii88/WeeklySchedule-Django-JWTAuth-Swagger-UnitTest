# Generated by Django 5.1.2 on 2024-10-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyschedule',
            name='friday',
            field=models.ManyToManyField(blank=True, related_name='friday_slots', to='app.timeslot'),
        ),
        migrations.AlterField(
            model_name='weeklyschedule',
            name='monday',
            field=models.ManyToManyField(blank=True, related_name='monday_slots', to='app.timeslot'),
        ),
        migrations.AlterField(
            model_name='weeklyschedule',
            name='saturday',
            field=models.ManyToManyField(blank=True, related_name='saturday_slots', to='app.timeslot'),
        ),
        migrations.AlterField(
            model_name='weeklyschedule',
            name='sunday',
            field=models.ManyToManyField(blank=True, related_name='sunday_slots', to='app.timeslot'),
        ),
        migrations.AlterField(
            model_name='weeklyschedule',
            name='thursday',
            field=models.ManyToManyField(blank=True, related_name='thursday_slots', to='app.timeslot'),
        ),
        migrations.AlterField(
            model_name='weeklyschedule',
            name='tuesday',
            field=models.ManyToManyField(blank=True, related_name='tuesday_slots', to='app.timeslot'),
        ),
        migrations.AlterField(
            model_name='weeklyschedule',
            name='wednesday',
            field=models.ManyToManyField(blank=True, related_name='wednesday_slots', to='app.timeslot'),
        ),
    ]
