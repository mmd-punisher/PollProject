from django import forms
from .models import Vote, Choice, UserModel


class VoteForm(forms.ModelForm):
    choice = forms.ModelChoiceField(
        queryset=Choice.objects.none(),
        widget=forms.RadioSelect(),
        empty_label=None
    )

    class Meta:
        model = Vote
        fields = ['choice']

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
