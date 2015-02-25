__author__ = 'mhelvey'
import django.forms
import django.utils.html as htmlUtil

class CustomForm(django.forms.Form):

    def __init__(self, request, *args, **kwargs):

        self.request = request
        # Call the super class
        super().__init__(*args, **kwargs)
        # Call the init method
        self.init()

    def __str__(self):
        return self.as_full()

    def init(self):
        print("init")

    def commit(self):
        print("commit")

    def as_full(self):
        html = []
        html.append('<form>')
        html.append('<div class="input-group">')
        for field in self.fields:
            html.append('<input type="text" class="form-control datepicker" placeholder="mm-dd-yy" aria-describedby="date-addon"/>')
        html.append('<input class="btn btn-primary btn-sm" type="submit" value="Save"/></div></form>')
        return htmlUtil.format_html(''.join(html))