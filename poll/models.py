from datetime import datetime, timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserModel(models.Model):
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
        ("di", "مطلقه"),
    ]
    JOB_CAT = [
        ('off', 'اداری'),
        ('eng', 'فنی'),
        ('pro', 'تولید'),
        ('ser', 'خدمات'),
    ]
    first_name = models.CharField(max_length=255, verbose_name="نام")
    last_name = models.CharField(max_length=255, verbose_name="نام خانوادگی")
    age = models.PositiveSmallIntegerField(verbose_name='سن',
                                           validators=[MinValueValidator(10, message='حداقل سن 10 سال است'),
                                                       MaxValueValidator(150,
                                                                         message='سن بیشتر از 150 سال قابل قبول نیست')])
    job_category = models.CharField(max_length=3, choices=JOB_CAT, verbose_name='رسته شغلی')
    job = models.CharField(max_length=255, verbose_name='شغل')
    organ = models.CharField(max_length=255, verbose_name='نام سازمان')

    work_experience = models.PositiveSmallIntegerField(default=0, verbose_name='سابقه شغلی',
                                                       validators=[MaxValueValidator(
                                                           60,
                                                           message='حداکثر سابقه شغلی 60 سال است')])
    education = models.CharField(max_length=2, choices=EDUCATION_Choices, verbose_name="تحصیلات")
    marital_status = models.CharField(max_length=2, choices=MARITAL_Choices, verbose_name="وضعیت تعهد")
    height = models.PositiveSmallIntegerField(verbose_name='قد (به سانتی متر)',
                                              validators=[MinValueValidator(110, message='حداقل قد 110 سانتی متر است'),
                                                          MaxValueValidator(
                                                              250,
                                                              message='قد وارد شده بیشتر از مقدار معقول است')])
    weight = models.FloatField(verbose_name='وزن (به کیلوگرم)',
                               validators=[MinValueValidator(20, message='وزن مورد نظر کمتر از مقدار معقول است'),
                                           MaxValueValidator(250, message='وزن وارد شده بیشتر از مقدار محدود شده است')])
    bmi = models.FloatField(null=True, blank=True, verbose_name='BMI')
    comment = models.CharField(null=True, blank=True, max_length=755, verbose_name='نظرات و پیشنهادات')
    date_join = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        ordering = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        self.bmi = round(self.weight / ((self.height / 100) ** 2), 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Question(models.Model):
    question_title = models.CharField(max_length=255, verbose_name='عنوان سوال')
    question_text = models.CharField(max_length=350, verbose_name='متن سوال')
    pub_date = models.DateTimeField(default=datetime.now, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'

    def __str__(self):
        return self.question_title


class Choice(models.Model):
    CHOICE_FIELDS = [
        ('0', 'هرگز'),
        ('1', 'به ندرت'),
        ('2', 'بعضی اوقات'),
        ('3', 'اغلب'),
        ('4', 'تقریبا همیشه'),
    ]
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال')
    choice_text = models.CharField(choices=CHOICE_FIELDS, max_length=1, verbose_name='متن گزینه ها')

    class Meta:
        verbose_name = 'انتخاب'
        verbose_name_plural = 'انتخاب ها'

    def __str__(self):
        return dict(self.CHOICE_FIELDS).get(self.choice_text, self.choice_text)


class Vote(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='کاربر')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='سوال')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='انتخاب')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ رای')
    box = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='تعداد ساعت کار')

    class Meta:
        verbose_name = 'رای'
        verbose_name_plural = 'رای ها'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.question.question_text} - {self.choice.choice_text}"
