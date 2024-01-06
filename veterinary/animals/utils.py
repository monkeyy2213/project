from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Услуги", 'url_name': 'service'},
        # {'title': "Добавить животное", 'url_name': 'add_animals'},
        # {'title': "Профиль", 'url_name': 'profile'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(2)
        #     user_menu.pop(2)

        context['menu'] = user_menu

        return context