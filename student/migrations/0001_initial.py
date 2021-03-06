# Generated by Django 3.2.4 on 2021-07-20 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('class1', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phoneno', models.IntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Compant_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('bond', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('careteria', models.CharField(max_length=200)),
                ('phoneno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Add_placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.compant_details')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.add_student')),
            ],
        ),
    ]
