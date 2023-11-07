# Generated by Django 4.2.7 on 2023-11-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='mood',
            field=models.CharField(choices=[('Happy', 'Happy'), ('Excited', 'Excited'), ('Sad', 'Sad'), ('Angry', 'Angry'), ('Irritated', 'Irritated'), ('Anxious', 'Anxious'), ('Stressed', 'Stressed')], max_length=100),
        ),
        migrations.AlterField(
            model_name='journal',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
