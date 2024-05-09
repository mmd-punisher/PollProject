from django.contrib import admin
from .models import Question, Choice, Vote, User

admin.site.site_header = 'CMDQ Administration'
admin.site.site_title = 'Voting Admin Area'
admin.site.index_title = 'Welcome to Voting Admin Area'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5
    verbose_name = 'Choice'
    verbose_name_plural = 'Choices'


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
# Vote Admin needed
admin.site.register(Vote)
# class VoteAdmin(admin.ModelAdmin):
admin.site.register(User)
