from django.db import models
from django.core.validators import RegexValidator

class daftar_pre_toefl(models.Model):
    nama_lengkap=models.CharField(verbose_name="Nama Lengkap",max_length=30)
    email=models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #message = models.CharField(max_length = 2000, default='Saya telah mendaftar kelas')

class daftar_english_todler(models.Model):
    nama_lengkap=models.CharField(verbose_name="Nama Lengkap",max_length=30)
    email=models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #message = models.CharField(max_length = 2000, default='Saya telah mendaftar kelas')

class daftar_pre_ielts(models.Model):
    nama_lengkap=models.CharField(verbose_name="Nama Lengkap",max_length=30)
    email=models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #message = models.CharField(max_length = 2000, default='Saya telah mendaftar kelas')



MC = 'MC'
CN = 'CN'
TX = 'TX'

CATEGORY = (
    (MC, 'Multichoice'),
    (CN, 'Choose N'),
    (TX, 'Text'),
)

VALYK = '1'
VALKA = '2'
VALKO = '3'
VALNE = '4'
VALVI = '5'

MULTICHOICE = (
    (VALYK, 'Least'),
    (VALKA, 'Less than average'),
    (VALKO, 'Average'),
    (VALNE, 'More than average'),
    (VALVI, 'Most'),
)

class Questionnaire(models.Model):
    questionnaire_name = models.CharField(max_length=100,
                                          verbose_name="Questionnaire",
                                          null=False,
                                          default=None,
                                          blank=False)
    def __str__(self):
        return self.questionnaire_name

class Question(models.Model):
    questionnaire = models.ManyToManyField(Questionnaire)
    question_text = models.CharField(max_length=200,
                                     verbose_name="Questionnaire name",
                                     null=True,
                                     default=None,
                                     blank=True)
    question_category = models.CharField(max_length=2,
                                         verbose_name="Question category",
                                         null=False,
                                         choices=CATEGORY,
                                         default=None,
                                         blank=False)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question)

class MultiChoiceAnswer(Answer):
    answer = models.IntegerField(choices=MULTICHOICE)
    def __str__(self):
        return self.answer