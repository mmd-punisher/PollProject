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
            'work_experience', 'education', 'marital_status', 'height', 'weight'
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control required'
    #         if self.errors.get(field_name):
    #             field.widget.attrs['class'] += ' is-invalid'
    #         field.widget.attrs['placeholder'] = field.label
    #         field.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control required'
            # field.widget.attrs['placeholder'] = field.label
            field.label = field.label


"""    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام', 'required': 'required'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی', 'required': 'required'})
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سن', 'required': 'required'})
    )
    job_category = forms.ChoiceField(
        choices=UserModel.JOB_CAT,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'رسته شغلی', 'required': 'required'})
    )
    job = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شغل', 'required': 'required'})
    )
    organ = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام سازمان', 'required': 'required'})
    )
    work_experience = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'سابقه شغلی', 'required': 'required'})
    )
    education = forms.ChoiceField(
        choices=UserModel.EDUCATION_Choices,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'تحصیلات', 'required': 'required'})
    )
    marital_status = forms.ChoiceField(
        choices=UserModel.MARITAL_Choices,
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'وضعیت تعهد', 'required': 'required'})
    )
    height = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'قد (به سانتی متر)', 'required': 'required'})
    )
    weight = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'وزن (به کیلوگرم)', 'required': 'required'})
    )
"""


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
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40})
        }
