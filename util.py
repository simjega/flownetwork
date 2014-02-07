import csv
import os


class Queue:

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

    def __str__(self):
        string = ''
        for x in self.list:
            string += str(x) + ' '
        return string


def parse(path):
    with open(path, 'rb') as csvfile:
        graphcsv = csv.reader(csvfile, delimiter=',')
        first = True
        e = []
        for row in graphcsv:
            if first:
                v = int(row[0].strip())
                first = False
            else:
                e.append(map((lambda x: int(x.strip())), row))
    return v, e


def makeAbsolutePath(path):
    if os.path.isabs(path):
        return path
    return os.getcwd() + '/' + path
