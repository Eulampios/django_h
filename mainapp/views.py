from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Заголовок новости 1',
                'description': 'Описание новости 1',
                'date': datetime.now()
            },  {
                'title': 'Заголовок новости 2',
                'description': 'Описание новости 2',
                'date': datetime.now()
            },  {
                'title': 'Заголовок новости 3',
                'description': 'Описание новости 3',
                'date': datetime.now()
            },  {
                'title': 'Заголовок новости 4',
                'description': 'Описание новости 4',
                'date': datetime.now()
            },  {
                'title': 'Заголовок новости 5',
                'description': 'Описание новости 5',
                'date': datetime.now()
            }
        ]
        return context_data
