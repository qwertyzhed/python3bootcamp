def ret_day(num):
    days = ['Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat', 'Sun']
    if num < 0 or num > 6:
        return 'not a day of the week'
    else:
        return days[num-1]


print(ret_day(2))
print(ret_day(-4))