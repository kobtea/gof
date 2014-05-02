#!/usr/bin/env python
import abc


class FileTreatmentException(Exception):
    pass


class Element(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def accept(self, visitor):
        pass


class Entry(Element):
    @abc.abstractmethod
    def get_size(self):
        pass

    def add(self, *args, **kwargs):
        raise FileTreatmentException

    def __iter__(self):
        raise FileTreatmentException

    def __str__(self):
        return '{} ({})'.format(self.name, self.get_size())


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def accept(self, visitor):
        visitor.visit_file(self)


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []

    def get_size(self):
        return sum(entry.get_size() for entry in self.directory)

    def add(self, entry):
        self.directory.append(entry)
        return self

    def accept(self, visitor):
        visitor.visit_dir(self)

    def __iter__(self):
        return iter(self.directory)


class ListVisitor:
    def __init__(self):
        self.current_dir = ''

    def visit_file(self, f):
        print('{}/{}'.format(self.current_dir, f))

    def visit_dir(self, d):
        print('{}/{}'.format(self.current_dir, d))
        save_dir = self.current_dir
        self.current_dir += '/{}'.format(d.name)
        for entry in iter(d):
            entry.accept(self)
        self.current_dir = save_dir


if __name__ == '__main__':
    print('Making root entries ...')
    dir_root = Directory('root')
    dir_bin = Directory('bin')
    dir_tmp = Directory('tmp')
    dir_usr = Directory('usr')
    dir_root.add(dir_bin)
    dir_root.add(dir_tmp)
    dir_root.add(dir_usr)
    dir_bin.add(File('vi', 10000))
    dir_bin.add(File('latex', 20000))
    dir_root.accept(ListVisitor())

    print('')
    print('Making user entries ...')
    dir_hogemi = Directory('hogemi')
    dir_foobar = Directory('foobar')
    dir_kobtea = Directory('kobtea')
    dir_usr.add(dir_hogemi)
    dir_usr.add(dir_foobar)
    dir_usr.add(dir_kobtea)
    dir_hogemi.add(File('diary.html', 100))
    dir_hogemi.add(File('Composite.py', 200))
    dir_foobar.add(File('memo.txt', 300))
    dir_foobar.add(File('game.doc', 400))
    dir_kobtea.add(File('junk.mkd', 500))
    dir_root.accept(ListVisitor())

    '''
    Making root entries ...
    /root (30000)
    /root/bin (30000)
    /root/bin/vi (10000)
    /root/bin/latex (20000)
    /root/tmp (0)
    /root/usr (0)

    Making user entries ...
    /root (31500)
    /root/bin (30000)
    /root/bin/vi (10000)
    /root/bin/latex (20000)
    /root/tmp (0)
    /root/usr (1500)
    /root/usr/hogemi (300)
    /root/usr/hogemi/diary.html (100)
    /root/usr/hogemi/Composite.py (200)
    /root/usr/foobar (700)
    /root/usr/foobar/memo.txt (300)
    /root/usr/foobar/game.doc (400)
    /root/usr/kobtea (500)
    /root/usr/kobtea/junk.mkd (500)
    '''
