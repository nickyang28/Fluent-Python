# -*- coding: utf-8 -*-
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time is come," the Walrus said,')
    for word in s:
        print(word)
    print(list(s))
