#!/usr/bin/env python3

def print_fibonacci(length):
    lst = [0, 1]
    if length < 3:
        lst = lst[0:length]
    else:
        for i in range(length - 2):
            lst.append(lst[-1] + lst[-2])
    print(lst)

def add_number():
    lst.append(lst[-1] + lst[-2])
    print(lst)

print_fibonacci(2)