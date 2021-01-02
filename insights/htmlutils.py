import constant


def create_html():
    with open(constant.HTML_TEMPLATE, 'r') as template:
        with open(constant.HTML_FILE, 'w') as htmlFile:
            for line in template:
                htmlFile.write(line)


def end_html():
    append_html('</body>' + "\n" + '</html>')
    print('HTML file is generated at ', constant.HTML_FILE)


def append_html(html_data):
    with open(constant.HTML_FILE, 'a+') as htmlFile:
        htmlFile.write(html_data)


class Heading:
    def __init__(self, text):
        append_html('<h3>' + text + '</h3>')


class Table:
    def __init__(self, caption):
        self.list_column_lists = []
        self.__header_columns = []
        self.__caption = caption
        self.html = '<table>'

    def add_header_row(self, header_columns_names):
        self.__header_columns = header_columns_names

    def add_column_data(self, column_data):
        self.list_column_lists.append(column_data)

    def write_html(self):
        self.html += '<caption>' + self.__caption + '</caption>' + "\n"
        self.__add_row(self.__header_columns, header=True)
        num_rows = len(self.list_column_lists[0])  # All columns have same length
        for index in range(num_rows):
            row = []
            for data_item_list in self.list_column_lists:
                row.append(data_item_list[index])
            self.__add_row(row)
        self.html += '</table>' + '</br>' + '</br>' + "\n"
        append_html(self.html)

    def __add_row(self, row, header=False):
        row_html = '    <tr>'
        table_data_start_tag = '<th>' if header else '<td>'
        table_data_end_tag = '</th>' if header else '</td>'
        for item in row:
            row_html += table_data_start_tag + str(item) + table_data_end_tag
        row_html += "\n"
        self.html += row_html
