from datetime import datetime, timedelta
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Vote, UserModel, Question, Choice
from django.utils.translation import gettext_lazy as _
from import_export.formats.base_formats import CSV, XLSX

from .resources import VoteResource

admin.site.site_header = 'پنل مدیریت CMDQ'
admin.site.site_title = 'پنل مدیریت نظرسنجی ادمین'
admin.site.index_title = 'به پنل مدیریت نظرسنجی ادمین خوش آمدید'


# ----------- user admin
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'age', 'job_category', 'job', 'organ', 'work_experience', 'education',
        'marital_status', 'height', 'weight', 'bmi', 'comment')
    list_filter = ('job', 'education', 'marital_status', 'organ')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


# ------------- question admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
    verbose_name = 'انتخاب'
    verbose_name_plural = 'انتخاب ها'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_title', 'question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_title', 'question_text', 'pub_date')
    ordering = ('id',)


# class VoteResource(resources.ModelResource):
#     user_first_name = fields.Field(
#         column_name='نام',
#         attribute='user',
#         widget=ForeignKeyWidget(UserModel, 'first_name'))
#     user_last_name = fields.Field(
#         column_name='نام خانوادگی',
#         attribute='user',
#         widget=ForeignKeyWidget(UserModel, 'last_name'))
#     user_organ = fields.Field(
#         column_name='نام سازمان',
#         attribute='user',
#         widget=ForeignKeyWidget(UserModel, 'organ'))
#     user_job_category = fields.Field(
#         column_name='رسته شغلی',
#         attribute='user',
#         widget=ForeignKeyWidget(UserModel, 'job_category'))
#     question_title = fields.Field(
#         column_name='عنوان سوال',
#         attribute='question',
#         widget=ForeignKeyWidget(Question, 'question_title'))
#     choice_text = fields.Field(
#         column_name='متن گزینه',
#         attribute='choice',
#         widget=ForeignKeyWidget(Choice, 'choice_text'))
#     vote_date = fields.Field(
#         column_name='تاریخ رای',
#         attribute='date')
#
#     class Meta:
#         model = Vote
#         fields = (
#             'user_first_name', 'user_last_name', 'user_organ', 'user_job_category', 'question_title', 'choice_text',
#             'vote_date')
#         export_order = (
#             'user_first_name', 'user_last_name', 'user_organ', 'user_job_category', 'question_title', 'choice_text',
#             'vote_date')


# --------------------- custom filters

class UserOrganFilter(admin.SimpleListFilter):
    title = 'نام سازمان'
    parameter_name = 'user_organ'

    def lookups(self, request, model_admin):
        organs = set(UserModel.objects.values_list('organ', flat=True))
        return [(organ, organ) for organ in organs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__organ=self.value())
        return queryset


class UserJobCategoryFilter(admin.SimpleListFilter):
    title = 'رسته شغلی'
    parameter_name = 'user_job_category'

    def lookups(self, request, model_admin):
        jobs = UserModel.JOB_CAT
        return jobs

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__job_category=self.value())
        return queryset


class VoteDateFilter(admin.SimpleListFilter):
    title = _('تاریخ رای')
    parameter_name = 'date'

    def lookups(self, request, model_admin):
        return [
            ('today', _('امروز')),
            ('yesterday', _('دیروز')),
            ('last_3_days', _('سه روز گذشته')),
            ('this_week', _('این هفته')),
            ('this_month', _('این ماه')),
            ('this_year', _('امسال')),
            ('past_7_days', _('هفته گذشته')),
            ('last_month', _('ماه گذشته')),
            ('last_year', _('سال گذشته')),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        today = datetime.today()
        if value == 'today':
            return queryset.filter(date__year=today.year, date__month=today.month, date__day=today.day)
        elif value == 'yesterday':
            yesterday = today - timedelta(days=1)
            return queryset.filter(date__year=yesterday.year, date__month=yesterday.month, date__day=yesterday.day)
        elif value == 'last_3_days':
            return queryset.filter(date__gte=today - timedelta(days=3))
        elif value == 'past_7_days':
            return queryset.filter(date__gte=today - timedelta(days=7))
        elif value == 'last_month':
            first_day_of_current_month = today.replace(day=1)
            last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
            first_day_of_last_month = last_day_of_last_month.replace(day=1)
            return queryset.filter(date__gte=first_day_of_last_month, date__lt=first_day_of_current_month)
        elif value == 'last_year':
            first_day_of_current_year = today.replace(month=1, day=1)
            last_day_of_last_year = first_day_of_current_year - timedelta(days=1)
            first_day_of_last_year = last_day_of_last_year.replace(month=1, day=1)
            return queryset.filter(date__gte=first_day_of_last_year, date__lt=first_day_of_current_year)
        elif value == 'this_week':
            start_of_week = today - timedelta(days=today.weekday())
            return queryset.filter(date__gte=start_of_week, date__lte=today)
        elif value == 'this_month':
            start_of_month = today.replace(day=1)
            return queryset.filter(date__gte=start_of_month, date__lte=today)
        elif value == 'this_year':
            start_of_year = today.replace(month=1, day=1)
            return queryset.filter(date__gte=start_of_year, date__lte=today)
        return queryset


# --------------- vote admin

# class VoteResource(resources.ModelResource):
#     user_ = fields.Field(attribute='user', column_name='کاربر')
#     user_organ_ = fields.Field(column_name='نام سازمان')
#     user_job_category_ = fields.Field(column_name='رسته شعلی')
#     user_job_ = fields.Field(column_name='شغل')
#     question_title_ = fields.Field(column_name='عنوان سوال')
#     choice_ = fields.Field(column_name='انتخاب')
#     date_ = fields.Field(column_name='تاریخ')
#
#     class Meta:
#         model = Vote
#         fields = ('user_', 'user_organ_', 'user_job_category_', 'user_job_', 'question_title_', 'choice_', 'date_')
#
#     encoding = 'utf-8'
#
#     def dehydrate_user_(self, obj):
#         return obj.user.first_name + ' ' + obj.user.last_name
#
#     def dehydrate_user_organ_(self, obj):
#         return obj.user.organ
#
#     def dehydrate_user_job_category_(self, obj):
#         return obj.user.job_category.value
#
#     def dehydrate_user_job_(self, obj):
#         return obj.user.job
#
#     def dehydrate_question_title_(self, obj):
#         return obj.question.question_title
#
#     def dehydrate_choice_(self, obj):
#         return obj.choice.choice_text
#
#     def dehydrate_date_(self, obj):
#         return obj.date.strftime('%Y-%m-%d')



@admin.register(Vote)
class VoteAdmin(ImportExportModelAdmin):
    resource_class = VoteResource
    list_display = ('user', 'user_organ', 'user_job_category', 'user_job', 'question', 'choice', 'date')
    list_filter = (UserOrganFilter, UserJobCategoryFilter, VoteDateFilter)
    ordering = ('-date',)

    def user_job(self, obj):
        return obj.user.job

    user_job.short_description = 'شغل'

    def user_organ(self, obj):
        return obj.user.organ

    user_organ.short_description = 'نام سازمان'

    def user_job_category(self, obj):
        return obj.user.get_job_category_display()

    user_job_category.short_description = 'رسته شغلی'
