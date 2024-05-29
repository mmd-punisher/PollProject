from django.contrib import admin
from django.http import HttpResponse
# from django.contrib.admin import DateFieldListFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
import csv
from .models import UserModel, Question, Choice, Vote

admin.site.site_header = 'پنل مدیریت CMDQ'
admin.site.site_title = 'پنل مدیریت نظرسنجی ادمین'
admin.site.index_title = 'به پنل مدیریت نظرسنجی ادمین خوش آمدید'


@admin.action(description='خروجی گرفتن (CSV)')
def export_users_to_csv(modeladmin, request, queryset):
    # Define the CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=users.csv'

    writer = csv.writer(response)
    # Retrieve all questions to dynamically create columns for answers
    questions = Question.objects.all()
    question_titles = [q.question_title for q in questions]

    # Write the header row
    header = [
                 'نام', 'نام خانوادگی', 'سن', 'رسته شغلی', 'شغل', 'نام سازمان',
                 'سابقه شغلی', 'تحصیلات', 'وضعیت تعهد', 'قد (به سانتی متر)', 'وزن (به کیلوگرم)',
                 'BMI', 'نظرات و پیشنهادات'
             ] + question_titles
    writer.writerow(header)

    # Write the user data rows
    for user in queryset:
        user_data = [
            user.first_name, user.last_name, user.age, user.get_job_category_display(),
            user.job, user.organ, user.work_experience, user.get_education_display(),
            user.get_marital_status_display(), user.height, user.weight,
            user.bmi, user.comment
        ]
        # Add answers to the questions
        for question in questions:
            try:
                vote = Vote.objects.get(user=user, question=question)
                user_data.append(vote.choice.choice_text if vote.choice else (vote.box if vote.box else ''))
            except Vote.DoesNotExist:
                user_data.append('')

        writer.writerow(user_data)

    return response


# ------------------------ User Admin
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'age', 'job_category', 'job', 'organ', 'work_experience', 'education',
        'marital_status', 'height', 'weight', 'bmi', 'comment'
    )
    actions = [export_users_to_csv]
    list_filter = (
        'job', 'education', 'marital_status', 'organ',
        ('vote__date', DateRangeFilter)
    )
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


# -------------------------- Vote Admin
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
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


# ------------- Question Choice Init
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
    verbose_name = 'انتخاب'
    verbose_name_plural = 'انتخاب ها'


# ------------- Question Admin
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_title', 'question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_title', 'question_text', 'pub_date')
    ordering = ('id',)
