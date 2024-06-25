from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserForm, VoteForm, CommentForm, VoteForm_2, VoteForm_3
from .models import UserModel, Question, Vote, Vote_2, Question_2, Question_3, Vote_3


def index(request):
    # return redirect('user_login')
    return render(request, 'poll/index.html')


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


def get_next_valid_question_id(question_id):
    next_question = Question.objects.filter(pk__gte=question_id).first()
    while next_question is None:
        question_id += 1
        next_question = Question.objects.filter(pk__gte=question_id).first()
        if Question.objects.filter(pk__gt=question_id).count() == 0:
            return None
    return next_question.pk


"""
# First Logic
def poll_view(request, question_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    user = get_object_or_404(UserModel, pk=user_id)

    question_id = get_next_valid_question_id(question_id)
    if question_id is None:
        return redirect('continue')

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
            next_question_id = get_next_valid_question_id(question_id + 1)
            if next_question_id:
                return redirect('poll', question_id=next_question_id)
            else:
                return redirect('continue')

    return render(request, 'poll/poll.html', {'form': form, 'question': question, 'user': user})


def poll_view_2(request, question_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    user = get_object_or_404(UserModel, pk=user_id)

    question = get_object_or_404(Question_2, pk=question_id)
    related_questions = Question_3.objects.filter(question_related=question)

    try:
        previous_vote = Vote_2.objects.get(user=user, question=question)
        form_2 = VoteForm_2(instance=previous_vote, question_id=question_id)
    except Vote_2.DoesNotExist:
        form_2 = VoteForm_2(question_id=question_id)

    forms_3 = []
    for related_question in related_questions:
        try:
            previous_vote = Vote_3.objects.get(user=user, question=related_question)
            form = VoteForm_3(instance=previous_vote, question_id=related_question.id,
                              prefix=f'question_{related_question.id}')
        except Vote_3.DoesNotExist:
            form = VoteForm_3(question_id=related_question.id, prefix=f'question_{related_question.id}')
        forms_3.append({'form': form, 'question': related_question})

    if request.method == 'POST':
        form_2 = VoteForm_2(request.POST, question_id=question_id)
        forms_3 = [{'form': VoteForm_3(request.POST, question_id=related_question.id,
                                       prefix=f'question_{related_question.id}'), 'question': related_question} for
                   related_question in related_questions]

        if form_2.is_valid() and all([item['form'].is_valid() for item in forms_3]):
            vote_2 = form_2.save(commit=False)
            vote_2.question = question
            vote_2.user = user
            vote_2.save()

            for item in forms_3:
                vote_3 = item['form'].save(commit=False)
                vote_3.question = item['question']
                vote_3.user = user
                vote_3.save()

            next_question = Question_2.objects.filter(pk__gt=question_id).first()
            if next_question:
                return redirect('poll_2', question_id=next_question.pk)
            else:
                return redirect('comment')

    return render(request, 'poll/poll.html', {
        'form_2': form_2,
        'forms_3': forms_3,
        'question': question,
        'user': user
    })
"""


def poll_view(request, question_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    user = get_object_or_404(UserModel, pk=user_id)

    question_id = get_next_valid_question_id(question_id)
    if question_id is None:
        return redirect('continue')

    question = get_object_or_404(Question, pk=question_id)

    try:
        previous_vote = Vote.objects.get(user=user, question=question)
        form = VoteForm(instance=previous_vote, question_id=question_id)
    except Vote.DoesNotExist:
        form = VoteForm(question_id=question_id)

    if request.method == 'POST':
        form = VoteForm(request.POST, question_id=question_id)
        if form.is_valid():
            # حذف رای قبلی
            Vote.objects.filter(user=user, question=question).delete()

            vote = form.save(commit=False)
            vote.question = question
            vote.user = user
            vote.save()
            next_question_id = get_next_valid_question_id(question_id + 1)
            if next_question_id:
                return redirect('poll', question_id=next_question_id)
            else:
                return redirect('continue')

    return render(request, 'poll/poll.html', {'form': form, 'question': question, 'user': user})


def poll_view_2(request, question_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    user = get_object_or_404(UserModel, pk=user_id)

    question = get_object_or_404(Question_2, pk=question_id)
    related_questions = Question_3.objects.filter(question_related=question)

    try:
        previous_vote = Vote_2.objects.get(user=user, question=question)
        form_2 = VoteForm_2(instance=previous_vote, question_id=question_id)
    except Vote_2.DoesNotExist:
        form_2 = VoteForm_2(question_id=question_id)

    forms_3 = []
    for related_question in related_questions:
        try:
            previous_vote = Vote_3.objects.get(user=user, question=related_question)
            form = VoteForm_3(instance=previous_vote, question_id=related_question.id,
                              prefix=f'question_{related_question.id}')
        except Vote_3.DoesNotExist:
            form = VoteForm_3(question_id=related_question.id, prefix=f'question_{related_question.id}')
        forms_3.append({'form': form, 'question': related_question})

    if request.method == 'POST':
        form_2 = VoteForm_2(request.POST, question_id=question_id)
        forms_3 = [{'form': VoteForm_3(request.POST, question_id=related_question.id,
                                       prefix=f'question_{related_question.id}'), 'question': related_question} for
                   related_question in related_questions]

        if form_2.is_valid() and all([item['form'].is_valid() for item in forms_3]):
            # حذف رای قبلی
            Vote_2.objects.filter(user=user, question=question).delete()
            vote_2 = form_2.save(commit=False)
            vote_2.question = question
            vote_2.user = user
            vote_2.save()

            for item in forms_3:
                # حذف رای قبلی
                Vote_3.objects.filter(user=user, question=item['question']).delete()
                vote_3 = item['form'].save(commit=False)
                vote_3.question = item['question']
                vote_3.user = user
                vote_3.save()

            next_question = Question_2.objects.filter(pk__gt=question_id).first()
            if next_question:
                return redirect('poll_2', question_id=next_question.pk)
            else:
                return redirect('comment')

    return render(request, 'poll/poll.html', {
        'form_2': form_2,
        'forms_3': forms_3,
        'question': question,
        'user': user
    })


def comment_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('user_login')
    user = get_object_or_404(UserModel, pk=user_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('complete')
    else:
        form = CommentForm(instance=user)

    return render(request, 'poll/comment.html', {'form': form})


def continue_view(request):
    return render(request, 'poll/continue.html', {'message': "Thank you, now get ready for the second part of poll!"})


def complete_view(request):
    return render(request, 'poll/complete.html', {'message': "از شما برای شرکت در این نظرسنجی سپاسگزاریم !"})


def contact_us(request):
    messages = {
        'product': 'طراحی و اجرا توسط علیرضا اسماعیلی و محمد موسی پور © '
    }
    return render(request, template_name='poll/contact_us.html', context=messages)


def about_us(request):
    message = {
    }
    return render(request, template_name='poll/about_us.html')


def site_header_partial(request):
    return render(request, 'shared/site_header_partial.html', {})
