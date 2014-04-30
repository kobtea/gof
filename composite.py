#!/usr/bin/env python
import abc


class FileTreatmentException(Exception):
    pass


class Entry(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_size(self):
        pass

    @abc.abstractmethod
    def print_list(self):
        pass

    def add(self, *args, **kwargs):
        raise FileTreatmentException

    def __str__(self):
        return '{} ({})'.format(self.name, self.get_size())


class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def print_list(self, prefix=''):
        print('{}/{}'.format(prefix, self))


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = []

    def get_size(self):
        return sum(entry.get_size() for entry in self.directory)

    def print_list(self, prefix=''):
        print('{}/{}'.format(prefix, self))
        for entry in self.directory:
            entry.print_list('{}/{}'.format(prefix, self.name))

    def add(self, entry):
        self.directory.append(entry)
        return self


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
    dir_root.print_list()

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
    dir_root.print_list()

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
