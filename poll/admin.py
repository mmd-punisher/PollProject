from django.contrib import admin
from django.http import HttpResponse
from rangefilter.filters import DateRangeFilter
import csv
from .models import UserModel, Question, Choice, Vote, Choice_2, Question_2, Vote_2, Question_3, Choice_3, Vote_3

admin.site.site_header = 'پنل مدیریت CMDQ'
admin.site.site_title = 'پنل مدیریت نظرسنجی ادمین'
admin.site.index_title = 'به پنل مدیریت نظرسنجی ادمین خوش آمدید'


@admin.action(description='خروجی گرفتن (CSV)')
def export_users_to_csv(modeladmin, request, queryset):
    # Define the CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=cmdq_output.csv'

    writer = csv.writer(response)
    # Retrieve all questions to dynamically create columns for answers and hours
    questions = list(Question.objects.all())
    questions_2 = list(Question_2.objects.all())
    questions_3 = list(Question_3.objects.all())

    # Write the header row
    header = [
        'نام', 'نام خانوادگی', 'سن', 'رسته شغلی', 'شغل', 'نام سازمان',
        'سابقه شغلی', 'تحصیلات', 'وضعیت تعهد', 'قد (به سانتی متر)', 'وزن (به کیلوگرم)',
        'جنسیت', 'BMI', 'نظرات و پیشنهادات'
    ]
    for question in questions:
        header.append(question.question_title)
        header.append(f"ساعت {question.question_title}")
    for question_2 in questions_2:
        header.append(question_2.question_title)
        for related_question in Question_3.objects.filter(question_related=question_2):
            header.append(related_question.question_title)
    writer.writerow(header)

    # Write the user data rows
    for user in queryset:
        user_data = [
            user.first_name, user.last_name, user.age, user.get_job_category_display(),
            user.job, user.organ, user.work_experience, user.get_education_display(),
            user.get_marital_status_display(), user.height, user.weight,
            user.get_gender_display(),  # Add gender display value here
            user.bmi, user.comment
        ]
        # Add answers to the questions
        for question in questions:
            try:
                vote = Vote.objects.get(user=user, question=question)
                user_data.append(vote.choice.choice_text if vote.choice else '')
                user_data.append(vote.box if vote.box else '')
            except Vote.DoesNotExist:
                user_data.append('')
                user_data.append('')
        for question_2 in questions_2:
            try:
                vote_2 = Vote_2.objects.get(user=user, question=question_2)
                user_data.append(vote_2.choice.choice_text if vote_2.choice else '')
                for related_question in Question_3.objects.filter(question_related=question_2):
                    try:
                        vote_3 = Vote_3.objects.get(user=user, question=related_question)
                        user_data.append(vote_3.choice.choice_text if vote_3.choice else '0')
                    except Vote_3.DoesNotExist:
                        user_data.append('0')
            except Vote_2.DoesNotExist:
                user_data.append('')
                for related_question in Question_3.objects.filter(question_related=question_2):
                    user_data.append('')

        writer.writerow(user_data)

    return response


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'age', 'job_category', 'job', 'organ', 'work_experience', 'education',
        'marital_status', 'height', 'weight', 'gender', 'bmi', 'comment'
    )
    actions = [export_users_to_csv]
    list_filter = (
        'job', 'education', 'marital_status', 'organ',
        ('vote__date', DateRangeFilter)
    )
    search_fields = ('first_name', 'last_name')
    ordering = ('-date_join', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)
        questions = Question.objects.all()
        questions_2 = Question_2.objects.all()
        for question in questions:
            field_name = f"question_{question.id}"
            box_field_name = f"question_box_{question.id}"
            self.list_display += (field_name, box_field_name)
            setattr(self, field_name, self._generate_question_display(question))
            setattr(self, box_field_name, self._generate_box_display(question))
        for question in questions_2:
            field_name = f"question_2_{question.id}"
            self.list_display += (field_name,)
            setattr(self, field_name, self._generate_question_2_display(question))
            for related_question in Question_3.objects.filter(question_related=question):
                related_field_name = f"related_question_{related_question.id}"
                self.list_display += (related_field_name,)
                setattr(self, related_field_name, self._generate_question_3_display(related_question))

    def _generate_question_display(self, question):
        def question_display(obj):
            vote = Vote.objects.filter(user=obj, question=question).first()
            if vote and vote.choice:
                return vote.choice.choice_text
            return "No answer"

        question_display.short_description = question.question_title
        return question_display

    def _generate_box_display(self, question):
        def box_display(obj):
            vote = Vote.objects.filter(user=obj, question=question).first()
            if vote and vote.box:
                return vote.box
            return "No hours"

        box_display.short_description = f"ساعت سوال {question.question_title}"
        return box_display

    def _generate_question_2_display(self, question):
        def question_2_display(obj):
            vote = Vote_2.objects.filter(user=obj, question=question).first()
            if vote and vote.choice:
                return vote.choice.choice_text
            return "No answer"

        question_2_display.short_description = question.question_title
        return question_2_display

    def _generate_question_3_display(self, related_question):
        def question_3_display(obj):
            vote = Vote_3.objects.filter(user=obj, question=related_question).first()
            if vote and vote.choice:
                return vote.choice.choice_text
            return "0"

        question_3_display.short_description = related_question.question_title
        return question_3_display


admin.site.register(UserModel, UserAdmin)


# ------------- Question Admin
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
    verbose_name = 'انتخاب'
    verbose_name_plural = 'انتخاب ها'


class ChoiceInline_2(admin.TabularInline):
    model = Choice_2
    extra = 5
    verbose_name = 'انتخاب'
    verbose_name_plural = 'انتخاب ها'


class ChoiceInline_3(admin.TabularInline):
    model = Choice_3
    extra = 3
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


@admin.register(Question_2)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline_2]
    list_display = ('question_title', 'pub_date', 'question_img')
    ordering = ('id',)


@admin.register(Question_3)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline_3]
    ordering = ('id',)
