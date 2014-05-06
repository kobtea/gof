#!/usr/bin/env python


class Database:
    @classmethod
    def get_properties(cls, email):
        return 'hogemi'


class HTMLWriter:
    @classmethod
    def title(cls, title):
        text = '''
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{0}</h1>
        '''.format(title)
        print(text)

    @classmethod
    def paragraph(cls, msg):
        print('<p>{}</p>'.format(msg))

    @classmethod
    def link(cls, href, caption):
        cls.paragraph('<a href="{}">{}</a>'.format(href, caption))

    @classmethod
    def mailto(cls, email, username):
        cls.link('mailto: {}'.format(email), username)

    @classmethod
    def close(cls):
        text = '''
    </body>
</html>
        '''
        print(text)


class PageMaker:
    @classmethod
    def make_welcome_page(cls, email):
        username = Database.get_properties(email)
        HTMLWriter.title("Welcome to {}'s page".format(username))
        HTMLWriter.paragraph('mail me !!')
        HTMLWriter.mailto(email, username)
        HTMLWriter.close()


if __name__ == '__main__':
    PageMaker.make_welcome_page('hogemi@hoge.mi')

    '''
<html>
    <head>
        <title>Welcome to hogemi's page</title>
    </head>
    <body>
        <h1>Welcome to hogemi's page</h1>

<p>mail me !!</p>
<p><a href="mailto: hogemi@hoge.mi">hogemi</a></p>

    </body>
</html>
    '''
