from django.db import models


class User(models.Model):
    EDUCATION_Choices = [
        ("hs", "تحصیلات دبیرستان"),
        ("di", "دیپلم"),
        ("bd", "کارشناسی"),
        ("ad", "کارشناسی ارشد"),
        ("dc", "دکتری و بالاتر"),
    ]
    MARITAL_Choices = [
        ("ma", "متعهد"),
        ("si", "مجرد"),
        ("di", "مطلفه"),
    ]
    first_name = models.CharField(max_length=255, verbose_name="نام")
    last_name = models.CharField(max_length=255, verbose_name="تام خانوادگی")
    age = models.PositiveSmallIntegerField(verbose_name='سن')
    job = models.CharField(max_length=255, null=True, verbose_name='شغل')
    work_experience = models.PositiveSmallIntegerField(default=0, null=True, verbose_name='سابقه شغلی')
    education = models.CharField(max_length=2, choices=EDUCATION_Choices, null=True, verbose_name="تحصیلات")
    marital_status = models.CharField(max_length=2, choices=MARITAL_Choices, null=True, verbose_name="وضعیت تعهد")
    height = models.PositiveSmallIntegerField(verbose_name='قد (به سانتی متر)')  # cm
    weight = models.FloatField(verbose_name='وزن (به متر)')
    bmi = models.FloatField(null=True, blank=True)


    def save(self, *args, **kwargs):
        self.bmi = self.weight / ((self.height / 100) ** 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.id}"

    class Meta:
        ordering = ['first_name', 'last_name']


class Question(models.Model):
    question_text = models.CharField(max_length=350)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=150)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.question.question_text} - {self.choice.choice_text}"