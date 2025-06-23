from django.contrib import admin
from .models import sgexam
from django.contrib.admin import DateFieldListFilter

@admin.register(sgexam)
class SgexamAdmin(admin.ModelAdmin):
    list_display = ('title', 'exam_date', 'created_date', 'is_public')
    search_fields = ('title', 'students__email')
    date_hierarchy = 'exam_date'
    filter_horizontal = ('students',)
    list_filter = (
        'is_public',
        ('created_date', DateFieldListFilter),
    )
    fieldsets = (
        (None, {
            'fields': ('title', 'exam_date', 'image')
        }),
        ('Настройки публикации', {
            'fields': ('is_public',)
        }),
        ('Студенты', {
            'fields': ('students',)
        }),
    )
