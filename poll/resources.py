from import_export import fields, resources
from import_export.formats.base_formats import XLSX
from tablib import Dataset

from poll.models import Vote


class UTF8XLSX(XLSX):
    def export_data(self, dataset, **kwargs):
        response = super().export_data(dataset, **kwargs)
        response.encoding = 'utf-8'
        return response


class VoteResource(resources.ModelResource):
    user = fields.Field(
        attribute='user', column_name='User')
    user_organ = fields.Field(
        attribute='user_organ', column_name='Organization')
    user_job_category = fields.Field(
        attribute='user_job_category', column_name='Job Category')
    user_job = fields.Field(
        attribute='user_job', column_name='Job')
    question_title = fields.Field(
        attribute='question_title', column_name='Question title')
    choice = fields.Field(
        attribute='choice', column_name='Choice')
    date = fields.Field(
        attribute='date', column_name='Date')

    class Meta:
        model = Vote
        fields = ('user', 'user_organ', 'user_job_category', 'user_job', 'question_title', 'choice', 'date')

        skip_unchanged = True
        report_skipped = False

    def dehydrate_user(self, obj):
        return obj.user.first_name + ' ' + obj.user.last_name

    def dehydrate_user_organ(self, obj):
        return obj.user.organ

    def dehydrate_user_job_category(self, obj):
        return obj.user.job_category

    def dehydrate_user_job(self, obj):
        return obj.user.job

    def dehydrate_question_title(self, obj):
        return obj.question.question_title

    def dehydrate_choice(self, obj):
        return obj.choice.choice_text

    def dehydrate_date(self, obj):
        return obj.date
