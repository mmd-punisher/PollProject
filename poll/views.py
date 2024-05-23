# views.py
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserForm, VoteForm
from .models import UserModel, Question, Vote


def index(request):
    return redirect('user_login')


def user_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.pk
            return redirect('poll', question_id=1)
    else:
        form = UserForm()
    return render(request, 'poll/login.html', {'form': form})


def poll_view(request, question_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    user = get_object_or_404(UserModel, pk=user_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        previous_vote = Vote.objects.get(user=user, question=question)
        form = VoteForm(instance=previous_vote, question_id=question_id)
    except Vote.DoesNotExist:
        form = VoteForm(question_id=question_id)
    if request.method == 'POST':
        form = VoteForm(request.POST, question_id=question_id)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.question = question
            vote.user = user
            vote.save()
            next_question = Question.objects.filter(pk__gt=question_id).first()
            if next_question:
                return redirect('poll', question_id=next_question.pk)
            else:
                return redirect('complete')
    return render(request, 'poll/poll.html', {'form': form, 'question': question, 'user': user})


def complete_view(request):
    return render(request, 'poll/complete.html', {'message': "Thank you for completing the survey!"})
