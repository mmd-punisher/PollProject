# Generated by Django 4.2.13 on 2024-06-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_alter_choice_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='box',
            field=models.PositiveSmallIntegerField(blank=True, max_length=2, null=True, verbose_name='تعداد ساعت کار'),
        ),
    ]
