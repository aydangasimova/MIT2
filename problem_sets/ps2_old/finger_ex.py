# Finger exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr , such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

import math

print("please input an integer")

number = int(input())


def sq_root(num):
    return print(math.sqrt(num))


def nth_root(num, pwr):
    answer = num**(1/pwr)
    return print(answer)


for pwr in range(1, 6):
    print("for pwr ", pwr, "root is", nth_root(number, pwr))
