_btd_sidebars = ['versions']
_btd_sidebars_extra = ['__buildthedocs_sidebar_'+t+'__.html'
                       for t in _btd_sidebars]
_btd_templates_extra = ['__buildthedocs_templates__']

try:
    templates_path = _btd_templates_extra + templates_path
except NameError:
    templates_path = _btd_templates_extra
except TypeError:
    templates_path = _btd_templates_extra + list(templates_path)

try:
    html_sidebars['**'] += _btd_sidebars_extra
except NameError:
    html_sidebar = {'**': _btd_sidebars_extra}
except (KeyError, TypeError):
    html_sidebars['**'] = _btd_sidebars_extra
except AttributeError:
    html_sidebars['**'] = list(html_sidebars['**'])+_btd_sidebars_extra

del _btd_sidebars
del _btd_sidebars_extra
del _btd_templates_extra
