#!/usr/bin/env python
import abc


class Builder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_title(self):
        pass

    @abc.abstractmethod
    def make_string(self):
        pass

    @abc.abstractmethod
    def make_items(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass


class TextBuilder(Builder):
    def __init__(self):
        self.text = []

    def make_title(self, string):
        self.text.append('=' * 40)
        self.text.append(string)
        self.text.append('-' * 40)

    def make_string(self, string):
        self.text.append(string)

    def make_items(self, string_list):
        for string in string_list:
            self.text.append('- {}'.format(string))

    def close(self):
        self.text.append('=' * 40)

    def get_result(self):
        return '\n'.join(self.text)


class HTMLBuilder(Builder):
    def __init__(self):
        self.html = []

    def make_title(self, string):
        s = '''
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{0}</h1>
        '''.format(string)
        self.html.append(s)

    def make_string(self, string):
        self.html.append('<p>{}</p>'.format(string))

    def make_items(self, string_list):
        self.html.append('<ul>')
        for string in string_list:
            self.html.append('<li>{}</li>'.format(string))
        self.html.append('</ul>')

    def close(self):
        s = '''
    </body>
</html>
        '''
        self.html.append(s)

    def get_result(self):
        return '\n'.join(self.html)


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.make_title('Builder Pattern Sample')
        self.builder.make_string('Sample Description')
        self.builder.make_items(['alma', 'blue', 'cirros'])
        self.builder.close()


if __name__ == '__main__':
    text_builder = TextBuilder()
    text_director = Director(text_builder)
    text_director.construct()
    print(text_builder.get_result())

    html_builder = HTMLBuilder()
    html_director = Director(html_builder)
    html_director.construct()
    print(html_builder.get_result())

    '''
========================================
Builder Pattern Sample
----------------------------------------
Sample Description
- alma
- blue
- cirros
========================================

<html>
    <head>
        <title>Builder Pattern Sample</title>
    </head>
    <body>
        <h1>Builder Pattern Sample</h1>

<p>Sample Description</p>
<ul>
<li>alma</li>
<li>blue</li>
<li>cirros</li>
</ul>

    </body>
</html>
    '''
