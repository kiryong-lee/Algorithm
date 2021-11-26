
import datetime

def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    diff = (datetime.date(2016, a, b) - datetime.date(2016, 1, 1)).days
    return day[diff % 7]
