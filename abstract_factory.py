#!/usr/bin/env python
import abc


# Abstract Factory
# ----------------
class Item(metaclass=abc.ABCMeta):
    def __init__(self, caption):
        self.caption = caption

    @abc.abstractmethod
    def make_html(self):
        pass


class Link(Item, metaclass=abc.ABCMeta):
    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url


class Tray(Item, metaclass=abc.ABCMeta):
    def __init__(self, caption):
        super().__init__(caption)
        self.tray = []

    def add(self, item):
        self.tray.append(item)


class Page(metaclass=abc.ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []

    def add(self, item):
        self.content.append(item)

    def output(self):
        print(self.make_html())

    @abc.abstractmethod
    def make_html(self):
        pass


class Factory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_link(self, caption, url):
        pass

    @abc.abstractmethod
    def create_tray(self, caption):
        pass

    @abc.abstractmethod
    def create_page(self, title, author):
        pass


# Concrete Factory
# ----------------
class ListLink(Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        s = '<li><a href="{}">{}</a></li>'.format(self.url,
                                                  self.caption)
        return s


class ListTray(Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        s = []
        s.append('<li>')
        s.append(self.caption)
        s.append('<ul>')
        for item in self.tray:
            s.append(item.make_html())
        s.append('</ul>')
        s.append('</li>')
        return '\n'.join(s)


class ListPage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        s = []
        html_begin = '''
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{0}</h1>
        <ul>
        '''.format(self.title)
        s.append(html_begin)
        for item in self.content:
            s.append(item.make_html())
        html_end = '''
        </ul>
        <hr/>
        <address>{0}</address>
    </body>
</html>
        '''.format(self.author)
        s.append(html_end)
        return '\n'.join(s)


class ListFactory(Factory):
    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, author):
        return ListPage(title, author)


def get_factory():
    return ListFactory()

if __name__ == '__main__':
    factory = get_factory()
    link_google = factory.create_link('google', 'http://google.com')
    link_yahoo = factory.create_link('yahoo', 'http://yahoo.com')
    link_myblog = factory.create_link('blog.kobtea.net',
                                      'http://blog.kobtea.net')

    tray_portal = factory.create_tray('Portal')
    tray_portal.add(link_google)
    tray_portal.add(link_yahoo)

    tray_blog = factory.create_tray('Blog')
    tray_blog.add(link_myblog)

    page = factory.create_page('Links', 'kobtea')
    page.add(tray_portal)
    page.add(tray_blog)
    page.output()

    '''
<html>
    <head>
        <title>Links</title>
    </head>
    <body>
        <h1>Links</h1>
        <ul>

<li>
Portal
<ul>
<li><a href="http://google.com">google</a></li>
<li><a href="http://yahoo.com">yahoo</a></li>
</ul>
</li>
<li>
Blog
<ul>
<li><a href="http://blog.kobtea.net">blog.kobtea.net</a></li>
</ul>
</li>

        </ul>
        <hr/>
        <address>kobtea</address>
    </body>
</html>
    '''
