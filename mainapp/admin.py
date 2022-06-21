from django.contrib import admin
from django.utils.html import format_html

from mainapp.models import News, Courses, Lesson, Teachers

# admin.site.register(News) класс для регистрации ниже
admin.site.register(Courses)
# admin.site.register(Lesson) класс для регистрации ниже
admin.site.register(Teachers)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted', 'preamble', 'slug', 'slug2')
    ordering = ('pk',)
    list_per_page = 3  # кол-во страниц
    list_filter = ('deleted', 'created')
    search_fields = ('title', 'preamble')
    actions = ('mark_as_delete',)

    def slug(self, object):
        return object.title.lower().replace(' ', '-')

    def slug2(self, object2):
        return format_html('<a href="{}" target="_blank">{}</a>',
                           object2.title.replace(' ', '-'), object2.title)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'пометить удаленным'  # для названия по-русски в меню

    slug.short_description = 'слаг'  # для заголовка
    slug2.short_description = 'слаг2'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'num', 'deleted', 'description')
    ordering = ('num',)
    list_filter = ('created', 'updated')
    list_per_page = 3
    search_fields = ('title', 'description')
    actions = ('mark_as_del',)

    def mark_as_del(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_del.short_description = 'пометить удаленным'
