class Table(list):

    def __str__(self):
        html = []
        html.append('<table class="table table-bordered table-striped">')
        for row in self:
            html.append('<tr>')
            for item in row:
                html.append('<td>{}</td>'.format(item))
            html.append('</tr>')
        html.append('</table>')
        return ''.join(html)