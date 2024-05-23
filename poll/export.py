from import_export.widgets import ForeignKeyWidget
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta
from import_export import resources, fields
from .models import Question, Choice, Vote, UserModel


# تعریف Resource برای Vote

class VoteResource(resources.ModelResource):
    user_first_name = fields.Field(
        column_name='نام',
        attribute='user',
        widget=ForeignKeyWidget(UserModel, 'first_name'))
    user_last_name = fields.Field(
        column_name='نام خانوادگی',
        attribute='user',
        widget=ForeignKeyWidget(UserModel, 'last_name'))
    user_organ = fields.Field(
        column_name='نام سازمان',
        attribute='user',
        widget=ForeignKeyWidget(UserModel, 'organ'))
    user_job_category = fields.Field(
        column_name='رسته شغلی',
        attribute='user',
        widget=ForeignKeyWidget(UserModel, 'job_category'))
    question_title = fields.Field(
        column_name='عنوان سوال',
        attribute='question',
        widget=ForeignKeyWidget(Question, 'question_title'))
    choice_text = fields.Field(
        column_name='متن گزینه',
        attribute='choice',
        widget=ForeignKeyWidget(Choice, 'choice_text'))

    class Meta:
        model = Vote
        fields = (
        'id', 'user_first_name', 'user_last_name', 'user_organ', 'user_job_category', 'question_title', 'choice_text',
        'date')
        export_order = (
        'id', 'user_first_name', 'user_last_name', 'user_organ', 'user_job_category', 'question_title', 'choice_text',
        'date')
