# Generated by Django 4.0.8 on 2024-03-28 09:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'User Progress', 'verbose_name_plural': 'User progress records'},
        ),
        migrations.AddField(
            model_name='progress',
            name='enrolled_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='exam.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='progress',
            name='score',
            field=models.CharField(default='', max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Score'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quizattempthistory',
            name='unattempted_question',
            field=models.CharField(max_length=1024, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')], verbose_name='UnAttempted Question List'),
        ),
    ]