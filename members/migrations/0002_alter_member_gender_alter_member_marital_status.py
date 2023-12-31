# Generated by Django 4.1.3 on 2023-07-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('S', 'Single'), ('R', 'Married'), ('D', 'Divorced')], max_length=200),
        ),
    ]
