# Generated by Django 4.2.3 on 2023-07-20 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=200, null=True)),
                ('hometown', models.CharField(max_length=200, null=True)),
                ('occupation', models.CharField(max_length=200, null=True)),
                ('educational_background', models.CharField(max_length=200, null=True)),
                ('house_number', models.CharField(max_length=20, null=True)),
                ('residental_area', models.CharField(max_length=200, null=True)),
                ('residental_street', models.CharField(max_length=200, null=True)),
                ('father_name', models.CharField(max_length=200, null=True)),
                ('father_hometown', models.CharField(max_length=200, null=True)),
                ('mother_name', models.CharField(max_length=200, null=True)),
                ('mother_hometown', models.CharField(max_length=200, null=True)),
                ('former_assembly', models.CharField(max_length=200, null=True)),
                ('former_district', models.CharField(max_length=200, null=True)),
                ('former_region_of_district_assembly', models.CharField(max_length=200, null=True)),
                ('place_of_baptism', models.CharField(max_length=200, null=True)),
                ('baptismal_officiating_minister', models.CharField(max_length=200, null=True)),
                ('zone', models.IntegerField()),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('R', 'Married'), ('D', 'Divorced')], max_length=200)),
                ('marital_officiating_minister', models.CharField(max_length=200, null=True)),
                ('place_of_marriage', models.CharField(max_length=200, null=True)),
                ('year_of_marriage_registered', models.DateField()),
                ('name_of_partner', models.CharField(max_length=200, null=True)),
                ('name_of_denomination_of_partner', models.CharField(max_length=200, null=True)),
                ('partner_hometown', models.CharField(max_length=100)),
            ],
        ),
    ]
