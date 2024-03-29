# Generated by Django 4.0.1 on 2022-01-18 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'el_course',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'el_student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'el_teacher',
            },
        ),
        migrations.CreateModel(
            name='Enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_enrolments', to='school.course')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_students', to='school.student')),
            ],
            options={
                'db_table': 'el_enrolment',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='tid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_teachers', to='school.teacher'),
        ),
    ]
