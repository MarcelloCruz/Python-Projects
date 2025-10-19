import math


def cin(): int(input())

def leapYear(n):
    return (n%4==0 and n%100!=0) or n%400==0

def main():
    year = cin()
    daynumber = cin()

    if leapYear(year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]

    else: month_days = [31 , 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]

    month = 1
    for days in month_days:
    if daynumber > days:
        daynumber -= days