#!/usr/bin/env python


class Book:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class BookShelf:
    def __init__(self):
        self.__book_list = []

    def append(self, book):
        self.__book_list.append(book)

    def find_by_index(self, index):
        try:
            return self.__book_list[index]
        except IndexError:
            return None

    def length(self):
        return len(self.__book_list)

    def iterator(self):
        return BookShelfIterator(self)


class BookShelfIterator:
    def __init__(self, bookshelf):
        self.__bookshelf = bookshelf
        self.__index = 0

    def has_next(self):
        return True if (self.__index < self.__bookshelf.length()) else False

    def next(self):
        next_book = self.__bookshelf.find_by_index(self.__index)
        self.__index += 1
        return next_book


if __name__ == '__main__':
    bookshelf = BookShelf()
    bookshelf.append('Article')
    bookshelf.append('Bible')
    bookshelf.append('Cinder')
    bookshelf_iter = bookshelf.iterator()
    while(bookshelf_iter.has_next()):
        print(bookshelf_iter.next())
