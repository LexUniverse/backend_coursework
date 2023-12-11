from .models import *

menu = [{'title': 'Логин', 'url_name': 'log'},
        {'title': 'Регистрация', 'url_name': 'reg'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu