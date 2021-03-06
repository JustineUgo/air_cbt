# Generated by Django 2.2.5 on 2020-07-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_examiner_name', models.CharField(max_length=200)),
                ('exam_code', models.CharField(max_length=200)),
                ('exam_name', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=False)),
                ('number_of_questions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examiner_code', models.CharField(max_length=200)),
                ('examiner_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_exam_name', models.CharField(max_length=50)),
                ('option_question_text', models.TextField(blank=True)),
                ('option_id', models.CharField(max_length=2)),
                ('option_text', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_exam_name', models.CharField(max_length=200)),
                ('question_text', models.TextField(blank=True)),
                ('question_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_question_code', models.CharField(max_length=200)),
                ('response_id', models.CharField(max_length=20)),
                ('response_text', models.TextField(blank=True)),
                ('status', models.IntegerField(default=0)),
                ('response_candidate_code', models.CharField(max_length=20)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=50)),
                ('student_rank', models.CharField(max_length=20)),
                ('student_level', models.CharField(max_length=20)),
                ('student_email', models.CharField(max_length=100)),
            ],
        ),
    ]
