#!/usr/bin/python3


def find_peak(list_of_integers):
    i = 0
    p = list_of_integers

    if type(p) is not list:
        return None
    if len(p) is 1:
        return p[0]
    for i in range(len(p) - 1):
        if len(p) == 0:
            return None
        if p[i] >= p[i - 1] and p[i] >= p[i + 1]:
            return p[i]
        if p[i - 1] > p[i - 2] and p[i - 1] > p[i]:
            return p[i - 1]
