from django.shortcuts import render
from .models import sgexam

# Create your views here.

def sgexam_list(request):
    exams = sgexam.objects.filter(is_public=True).order_by('-exam_date')
    context = {
        'exams': exams,
        'fio': 'Савиди Георгий',  # Замените на ваши ФИО
        'group': '123-ИВТ',       # Замените на ваш номер группы
    }
    return render(request, 'main/sgexam_list.html', context)
