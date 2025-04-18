# Generated by Django 4.2.4 on 2024-12-28 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QPaperAnalyzerApp', '0009_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=200)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('scheduled_date', models.DateField()),
                ('max_score', models.IntegerField()),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='QPaperAnalyzerApp.college')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='QPaperAnalyzerApp.course')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='QPaperAnalyzerApp.profile')),
            ],
        ),
    ]
