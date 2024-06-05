from django import forms
from .models import Vote, Choice, UserModel, Choice_2, Vote_2, Choice_3, Vote_3


class VoteForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.none(),
        widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Vote
        fields = ['choice', 'box']

    def __init__(self, *args, **kwargs):
        question_id = kwargs.pop('question_id')
        super().__init__(*args, **kwargs)
        self.fields['choice'].queryset = Choice.objects.filter(question_id=question_id)


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel

        fields = [
            'first_name', 'last_name', 'age', 'job_category', 'job', 'organ',
            'work_experience', 'education', 'marital_status', 'height', 'weight']


class VoteForm_2(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice_2.objects.none(),
        widget=forms.RadioSelect(),
        empty_label=None
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
        empty_label=None
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
