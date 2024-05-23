from import_export.admin import ImportExportModelAdmin
from .resources import VoteResource
from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ExportMixin
from .models import UserModel, Question, Choice, Vote
from import_export.widgets import Widget

admin.site.site_header = 'پنل مدیریت CMDQ'
admin.site.site_title = 'پنل مدیریت نظرسنجی ادمین'
admin.site.index_title = 'به پنل مدیریت نظرسنجی ادمین خوش آمدید'


# ----------- user admin
# @admin.register(UserModel)
# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         'first_name', 'last_name', 'age', 'job_category', 'job', 'organ', 'work_experience', 'education',
#         'marital_status', 'height', 'weight', 'bmi', 'comment')
#     list_filter = ('job', 'education', 'marital_status', 'organ')
#     search_fields = ('first_name', 'last_name')
#     ordering = ('first_name', 'last_name')


class QuestionWidget(Widget):
    def __init__(self, question):
        self.question = question

    def render(self, value, obj=None):
        vote = Vote.objects.filter(user=obj, question=self.question).first()
        if vote and vote.choice:
            return vote.choice.choice_text
        return "No answer"


class UserResource(resources.ModelResource):
    class Meta:
        model = UserModel
        fields = (
            'first_name', 'last_name', 'age', 'job_category', 'job', 'organ', 'work_experience', 'education',
            'marital_status', 'height', 'weight', 'bmi', 'comment'
        )

    def __init__(self, *args, **kwargs):
        super(UserResource, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            field_name = f"question_{question.id}"
            self.fields[field_name] = fields.Field(
                column_name=question.question_title,
                attribute=None,
                widget=QuestionWidget(question)
            )


class UserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = UserResource
    list_display = (
        'first_name', 'last_name', 'age', 'job_category', 'job', 'organ', 'work_experience', 'education',
        'marital_status', 'height', 'weight', 'bmi', 'comment'
    )
    list_filter = ('job', 'education', 'marital_status', 'organ')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            field_name = f"question_{question.id}"
            self.list_display += (field_name,)
            setattr(self, field_name, self._generate_question_display(question))

    def _generate_question_display(self, question):
        def question_display(obj):
            vote = Vote.objects.filter(user=obj, question=question).first()
            if vote and vote.choice:
                return vote.choice.choice_text
            return "No answer"

        question_display.short_description = question.question_title
        return question_display


admin.site.register(UserModel, UserAdmin)


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


# --------------- vote admin (Worked Without Filtering)
# export btn
# @admin.register(Vote)
# class VoteAdmin(ImportExportModelAdmin):
#     resource_class = VoteResource
#     list_display = ('user', 'user_organ', 'user_job_category', 'user_job', 'question', 'choice', 'date')
#     list_filter = (UserOrganFilter, UserJobCategoryFilter, VoteDateFilter)
#     ordering = ('-date',)
#
#     def user_job(self, obj):
#         return obj.user.job
#
#     user_job.short_description = 'شغل'
#
#     def user_organ(self, obj):
#         return obj.user.organ
#
#     user_organ.short_description = 'نام سازمان'
#
#     def user_job_category(self, obj):
#         return obj.user.get_job_category_display()
#
#     user_job_category.short_description = 'رسته شغلی'

@admin.register(Vote)
class VoteAdmin(ImportExportModelAdmin):
    resource_class = VoteResource
    list_display = ('user', 'user_organ', 'user_job_category', 'user_job', 'question', 'choice', 'date')
    list_filter = ('user__organ', 'user__job_category', 'date')
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

    def get_export_queryset(self, request):
        qs = super().get_export_queryset(request)
        return self.get_queryset(request).filter(pk__in=qs)

# export action (not good)

# @admin.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
#     list_display = ('user', 'user_organ', 'user_job_category', 'user_job', 'question', 'choice', 'date')
#     list_filter = (UserOrganFilter, UserJobCategoryFilter, VoteDateFilter)
#     ordering = ('-date',)
#     actions = ['export_as_csv']
#
#     def export_as_csv(self, request, queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]
#
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)
#
#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])
#
#         return response
#
#     export_as_csv.short_description = "خروجی اکسل"
#
#     def user_job(self, obj):
#         return obj.user.job
#
#     user_job.short_description = 'شغل'
#
#     def user_organ(self, obj):
#         return obj.user.organ
#
#     user_organ.short_description = 'نام سازمان'
#
#     def user_job_category(self, obj):
#         return obj.user.get_job_category_display()
#
#     user_job_category.short_description = 'رسته شغلی'
