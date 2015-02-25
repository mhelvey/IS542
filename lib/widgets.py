__author__ = 'mhelvey'
import django.forms
from django.forms.util import flatatt
import django.forms.widgets
from django.utils.encoding import force_text
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
import itertools


'''I got a lot of this code from island on github... Hopefully that is ok. '''
class DatePickWidget(django.forms.TextInput):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, choices=()):
        output = []
        output.append(format_html('<div{0}>'))
        options = self.render_options(attrs['id'], name, choices, [value])
        if options:
            output.append(options)
            output.append('</div>')
        return mark_safe('\n'.join(output))

    def render_options(self, elem_id, name, choices, selected_choices):
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        for i, (option_value, option_label) in enumerate(itertools.chain(self.choices, choices)):
            option_value = force_text(option_value)
            btn_class = mark_safe(self.btn_class)
            checked = ''
            if option_value in selected_choices:
                btn_class = mark_safe('%s %s' % (btn_class, 'active'))
                checked = 'checked'
            output.append(format_html('<label class="{0}"><input type="radio" value="{1}" name="{2}" id="{3}" {4} autocomplete="off"/>{5}</label>',
                             btn_class,
                             option_value,
                             name,
                             '%s_%s' % (elem_id, i),
                             checked,
                             option_label))
        return '\n'.join(output)

    class WidgetMedia:
        css = {
            'all': ('css/jquery-ui.min.css', 'css/jquery-ui.theme.min.css'),
        }
        js = ('js/jquery-ui.min.js', 'js/datepicker.js')