from django.utils.html import format_html


class Table(list):

    headers = ['First Name', 'Last Name', 'Email Address']


    def __str__(self):
        html = []
        html.append('<table class="table table-bordered table-striped">')

        # wirte headers
        html.append('<tr>')
        for item in self.headers:
            html.append('<th>{}</th>'.format(item))
        html.append('</tr>')

        # write the data
        for row in self:
            html.append('<tr>')
            for item in row:
                html.append('<td>{}</td>'.format(item))
            html.append('</tr>')
        html.append('</table>')
        return format_html(''.join(html))