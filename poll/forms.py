from django import forms
from .models import Vote, Choice, UserModel, Choice_2, Vote_2, Choice_3, Vote_3


class VoteForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.none(),
        widget=forms.RadioSelect(attrs={'class': 'form-group justify-content-end'}),
        empty_label=None,
        label='',
        required=True,
    )

    class Meta:
        model = Vote
        fields = ['choice', 'box']

    box = forms.IntegerField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'چند ساعت در روز', 'required': False}),
    )

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice.objects.filter(question_id=question_id)


"""class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 'age', 'job_category', 'job', 'organ',
            'work_experience', 'education', 'marital_status', 'height', 'weight'
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control required'
            field.required = True
"""


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'first_name', 'last_name', 'age', 'job_category', 'job', 'organ',
            'work_experience', 'education', 'marital_status', 'height', 'weight', 'gender'
        ]
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'form-control required'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control required'
            if field_name == 'job_category':
                field.choices = [('', 'رسته شغلی')] + list(field.choices)[1:]
            if field_name == 'education':
                field.choices = [('', 'میزان تحصیلات')] + list(field.choices)[1:]
            if field_name == 'marital_status':
                field.choices = [('', 'وضعیت تاهل')] + list(field.choices)[1:]
            if field_name == 'gender':
                field.choices = [('', 'جنسیت')] + list(field.choices)[1:]
            else:
                field.widget.attrs['placeholder'] = field.label
            field.label = ''


class VoteForm_2(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice_2.objects.none(),
        widget=forms.RadioSelect(),
        empty_label=None,
        label='',
        required=True,
    )

    class Meta:
        model = Vote_2
        fields = ['choice']

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice_2.objects.filter(question_id=question_id)


class VoteForm_3(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice_3.objects.none(),
        widget=forms.RadioSelect(),
        empty_label=None,
        label='',
        required=False  # Set required to False
    )

    class Meta:
        model = Vote_3
        fields = ['choice']

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice_3.objects.filter(question_id=question_id)


class CommentForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 12,
                'cols': 70,
                'dir': 'rtl',
                'placeholder': 'نظرات خود را با ما به اشتراک بگذارید...'
            }),
        }
