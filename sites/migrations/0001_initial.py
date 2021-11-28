# Generated by Django 2.2.7 on 2021-11-17 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afocha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Afocha Name')),
            ],
        ),
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efname', models.CharField(max_length=100, verbose_name='English First Name')),
                ('elname', models.CharField(max_length=100, verbose_name='English Last  Name')),
                ('role_num', models.IntegerField(unique=True, verbose_name='Role Number')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, verbose_name='Gender')),
                ('dod', models.DateField(verbose_name='Date of Death')),
                ('grave_number', models.IntegerField(verbose_name='Grave Number')),
                ('qebele', models.IntegerField(verbose_name='Qebele')),
                ('afocha_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Afocha')),
            ],
        ),
    ]