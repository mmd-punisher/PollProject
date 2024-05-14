from django.contrib import admin
from .models import Question, Choice, Vote, User

# admin.site.site_header = 'CMDQ Administration'
admin.site.site_header = 'پنل مدیریت CMDQ'
admin.site.site_title = 'پنل مدیریت نظرسنجی ادمین'
admin.site.index_title = 'به پنل مدیریت نظرسنجی ادمین خوش آمدید'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
    verbose_name = 'انتخاب'
    verbose_name_plural = 'انتخاب ها'


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date',)
    ordering = ('id',)


class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'question__id', 'question', 'choice')
    list_filter = ('user', 'question__id', 'choice', 'question')
    ordering = ('-user', 'question__id')

    # @staticmethod
    # def user__id(self, obj):
    #     return obj.user.id

    def question__id(self, obj):
        return obj.question.id


admin.site.register(Vote, VoteAdmin)

admin.site.register(Question, QuestionAdmin)
# Vote Admin needed
# admin.site.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
admin.site.register(User)
