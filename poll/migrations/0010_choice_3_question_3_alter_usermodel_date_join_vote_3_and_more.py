# Generated by Django 4.2.13 on 2024-06-05 08:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0009_alter_usermodel_date_join'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(choices=[('0', 'هرگز/کم'), ('1', 'متوسط'), ('2', 'زیاد')], max_length=1, verbose_name='متن گزینه ها')),
            ],
            options={
                'verbose_name': 'انتخاب',
                'verbose_name_plural': 'انتخاب ها',
            },
        ),
        migrations.CreateModel(
            name='Question_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=255, verbose_name='عنوان سوال')),
                ('question_text', models.CharField(max_length=350, verbose_name='متن سوال')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='تاریخ انتشار')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوالات سری سوم',
            },
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='date_join',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 5, 12, 16, 2, 262711)),
        ),
        migrations.CreateModel(
            name='Vote_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ رای')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.choice_3', verbose_name='انتخاب')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.question_3', verbose_name='سوال')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.usermodel', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'رای',
                'verbose_name_plural': 'رای ها',
            },
        ),
        migrations.AddField(
            model_name='choice_3',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.question_3', verbose_name='سوال'),
        ),
    ]
