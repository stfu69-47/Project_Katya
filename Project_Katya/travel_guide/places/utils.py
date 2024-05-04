mainmenu = [
    {'id': 1, 'name': 'Места', "url_name": 'places'},
    {'id': 2, 'name': 'Добавление статьи', "url_name": 'addplace'},
    {'id': 3, 'name': 'Добавление человека', "url_name": 'addperson'},
    {'id': 4, 'name': 'Контакты', "url_name": 'contact'},
    {'id': 5, 'name': 'Обратная связь', "url_name": 'feedback'},
    {'id': 6, 'name': 'О сайте', "url_name": 'about'},
]

contacts = [
    {'title': 'Администратор', 'name': 'Парфенова Е.А.'},
    {'title': 'Менеджер', 'name': 'Трофимов А.А.'},
    {'title': 'Корреспондент', 'name': 'Зелибоба П.П.'},
]

feedback = [
    {'title': 'Почта', 'content': 'tili_pili@mail.ru'},
    {'title': 'Телефон', 'content': '8-800-555-35-35'},
    {'title': 'ВК', 'content': 'https://www.vk.com'},
]


class DataMixin:
    title_page = None
    extra_context = {}
    paginate_by = 3

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'contacts' not in self.extra_context:
            self.extra_context['contacts'] = contacts

        if 'feedback' not in self.extra_context:
            self.extra_context['feedback'] = feedback

    def get_mixin_context(self, context, **kwargs):
        context['feedback'] = feedback
        context['contacts'] = contacts
        context.update(kwargs)
        return context
