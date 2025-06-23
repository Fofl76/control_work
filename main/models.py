from django.db import models
from django.contrib.auth.models import User

class sgexam(models.Model):
    title = models.CharField('Название экзамена', max_length=200)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    exam_date = models.DateTimeField('Дата проведения экзамена')
    image = models.ImageField('Изображение задания', upload_to='exam_images/')
    students = models.ManyToManyField(User, verbose_name='Студенты')
    is_public = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'
