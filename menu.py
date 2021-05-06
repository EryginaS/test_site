"""
This file was generated with the custommenu management command, it contains
the classes for the admin menu, you can customize this class as you want.

To activate your custom menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'samplesite.menu.CustomMenu'
"""

try:
    # we use django.urls import as version detection as it will fail on django 1.11 and thus we are safe to use
    # gettext_lazy instead of ugettext_lazy instead
    from django.urls import reverse
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.core.urlresolvers import reverse
    from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    """
    Custom Menu for samplesite admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            # items.Bookmarks(),
            
            items.ModelList(
                'Управление', ['bboard.models.Applications', 'bboard.models.Clients', 'bboard.models.ItPerson'], 
                exclude=['bboard.models.Dept']
            ),
            items.ModelList(
                'Пользователи и группы', ['django.contrib.auth.*',]
            ), 
            items.MenuItem(('Отчеты'), reverse('bboard:login'))
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)