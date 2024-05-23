from import_export import fields, resources
from poll.models import Vote
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta


class VoteResource(resources.ModelResource):
    # For exporting to csv
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
        return obj.user.get_job_category_display()

    def dehydrate_user_job(self, obj):
        return obj.user.job

    def dehydrate_question_title(self, obj):
        return obj.question.question_title

    def dehydrate_choice(self, obj):
        return obj.choice.choice_text

    def dehydrate_date(self, obj):
        return obj.date


# ---------------------------- use filter in output

"""
class DateRangeFilter(admin.SimpleListFilter):
    title = _('تاریخ')
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return [
            ('today', _('امروز')),
            ('yesterday', _('روز گذشته')),
            ('past_7_days', _('هفت روز گذشته')),
            ('this_month', _('این ماه')),
            ('past_30_days', _('سی روز گذشته')),
        ]

    def queryset(self, request, queryset):
        today = datetime.now().date()
        if self.value() == 'today':
            return queryset.filter(date__date=today)
        elif self.value() == 'yesterday':
            yesterday = today - timedelta(days=1)
            return queryset.filter(date__date=yesterday)
        elif self.value() == 'past_7_days':
            start_date = today - timedelta(days=7)
            return queryset.filter(date__date__gte=start_date)
        elif self.value() == 'this_month':
            start_date = today.replace(day=1)
            return queryset.filter(date__date__gte=start_date)
        elif self.value() == 'past_30_days':
            start_date = today - timedelta(days=30)
            return queryset.filter(date__date__gte=start_date)
        return queryset
"""